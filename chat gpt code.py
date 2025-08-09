"""
Jetpack Cat Runner
A complete single-file Python game using pygame.

Features:
- Jetpack Cat character (simple shapes, no external assets)
- Running + Jump + Duck + Dash
- Obstacles (drones, laser gates)
- Power-ups (magnet, shield, turbo)
- Coins to collect
- Day/Night cycle
- Smooth speed scaling and score multiplier

Controls:
- SPACE / W / UP: Jump (single jump, can upgrade to double if you want)
- DOWN / S: Duck (hold)
- LSHIFT / RSHIFT: Dash (short speed burst)
- ESC or close window: Quit

Requirements:
- Python 3.8+
- pygame (install with `pip install pygame`)

Run:
- Save this file as `jetpack_cat_runner.py` and run `python jetpack_cat_runner.py`.

Notes:
- This file uses only pygame and draws everything with primitives so you don't need image files.
- Tweak constants in the SETTINGS section near the top for difficulty, sizes, spawn rates, etc.

"""

import pygame
import random
import math
import sys
from collections import deque

# ===================== SETTINGS =====================
WIDTH, HEIGHT = 900, 480
FPS = 60
GROUND_Y = HEIGHT - 80

# Gameplay tuning
INITIAL_SCROLL_SPEED = 6.0
SPEED_INCREASE_RATE = 0.0005  # per frame
OBSTACLE_SPAWN_RATE = 1500  # milliseconds (approx)
POWERUP_SPAWN_RATE = 7000  # milliseconds
COIN_SPAWN_RATE = 900  # milliseconds

# Player
PLAYER_W, PLAYER_H = 60, 48
JUMP_VELOCITY = -13
GRAVITY = 0.7
DASH_MULT = 2.3
DASH_DURATION = 350  # ms
DUCK_HEIGHT = 28

# Powerup durations (ms)
SHIELD_DURATION = 4000
MAGNET_DURATION = 5000
TURBO_DURATION = 3000

# Colors
WHITE = (245, 245, 245)
BLACK = (10, 10, 10)
SKY_DAY = (135, 206, 235)
SKY_NIGHT = (18, 24, 58)
GROUND_COLOR = (40, 40, 40)

# ====================================================

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jetpack Cat Runner")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)
large_font = pygame.font.SysFont(None, 48)

# Events
SPAWN_OBSTACLE = pygame.USEREVENT + 1
SPAWN_POWERUP = pygame.USEREVENT + 2
SPAWN_COIN = pygame.USEREVENT + 3
pygame.time.set_timer(SPAWN_OBSTACLE, OBSTACLE_SPAWN_RATE)
pygame.time.set_timer(SPAWN_POWERUP, POWERUP_SPAWN_RATE)
pygame.time.set_timer(SPAWN_COIN, COIN_SPAWN_RATE)

# Helper functions

def draw_text(surf, text, x, y, color=WHITE, size=24, right=False):
    f = pygame.font.SysFont(None, size)
    r = f.render(text, True, color)
    rect = r.get_rect()
    if right:
        rect.topright = (x, y)
    else:
        rect.topleft = (x, y)
    surf.blit(r, rect)


# Classes
class Player:
    def __init__(self):
        self.x = 120
        self.y = GROUND_Y - PLAYER_H
        self.w = PLAYER_W
        self.h = PLAYER_H
        self.vy = 0
        self.on_ground = True
        self.ducking = False
        self.dashing = False
        self.dash_end_time = 0
        self.shield = False
        self.shield_end = 0
        self.magnet = False
        self.magnet_end = 0
        self.turbo = False
        self.turbo_end = 0
        self.score = 0

    def rect(self):
        return pygame.Rect(self.x, self.y, self.w, self.h if not self.ducking else DUCK_HEIGHT)

    def jump(self):
        if self.on_ground:
            self.vy = JUMP_VELOCITY
            self.on_ground = False

    def duck(self, val: bool):
        if self.on_ground:
            self.ducking = val

    def start_dash(self, now_ms):
        if not self.dashing:
            self.dashing = True
            self.dash_end_time = now_ms + DASH_DURATION

    def update(self, dt, now_ms):
        # Gravity
        if not self.on_ground:
            self.vy += GRAVITY
            self.y += self.vy
            if self.y >= GROUND_Y - (DUCK_HEIGHT if self.ducking else self.h):
                self.y = GROUND_Y - (DUCK_HEIGHT if self.ducking else self.h)
                self.vy = 0
                self.on_ground = True
        # Powerup timeouts
        if self.shield and now_ms > self.shield_end:
            self.shield = False
        if self.magnet and now_ms > self.magnet_end:
            self.magnet = False
        if self.turbo and now_ms > self.turbo_end:
            self.turbo = False
        if self.dashing and now_ms > self.dash_end_time:
            self.dashing = False

    def draw(self, surf, now_ms):
        r = self.rect()
        # body
        pygame.draw.rect(surf, (220, 120, 220), r, border_radius=8)
        # face
        face = pygame.Rect(r.x + 6, r.y + 6, 20, 18)
        pygame.draw.rect(surf, (255, 230, 200), face, border_radius=6)
        # ear
        pygame.draw.polygon(surf, (220, 120, 220), [(r.x+6, r.y+6), (r.x+2, r.y-6), (r.x+16, r.y+2)])
        # jetpack flame when in air or dashing
        if not self.on_ground or self.dashing or (pygame.key.get_pressed()[pygame.K_LSHIFT] or pygame.key.get_pressed()[pygame.K_RSHIFT]):
            flame_h = 12 + (5 if self.dashing else 0)
            pygame.draw.polygon(surf, (255, 165, 0), [(r.right - 6, r.y + r.h//2 - 4), (r.right + flame_h, r.y + r.h//2), (r.right - 6, r.y + r.h//2 + 4)])
        # shield
        if self.shield:
            pygame.draw.ellipse(surf, (150, 200, 255), r.inflate(14, 18), 3)


class Obstacle:
    def __init__(self, kind, x, y, w, h, speed):
        self.kind = kind
        self.rect = pygame.Rect(x, y, w, h)
        self.speed = speed

    def update(self, dt):
        self.rect.x -= self.speed * dt

    def draw(self, surf):
        if self.kind == 'drone':
            pygame.draw.rect(surf, (200, 60, 60), self.rect, border_radius=6)
            # propellers
            pygame.draw.circle(surf, (40,40,40), (self.rect.centerx - 18, self.rect.top+6), 6)
            pygame.draw.circle(surf, (40,40,40), (self.rect.centerx + 18, self.rect.top+6), 6)
        elif self.kind == 'laser':
            pygame.draw.rect(surf, (255, 30, 30), self.rect)
            pygame.draw.rect(surf, (20,20,20), (self.rect.x, self.rect.y + self.rect.h//2 - 4, self.rect.w, 8))


class Powerup:
    def __init__(self, ptype, x, y, speed):
        self.ptype = ptype
        self.x = x
        self.y = y
        self.speed = speed
        self.rect = pygame.Rect(x, y, 28, 28)

    def update(self, dt):
        self.x -= self.speed * dt
        self.rect.x = int(self.x)

    def draw(self, surf):
        if self.ptype == 'shield':
            pygame.draw.rect(surf, (120,190,255), self.rect, border_radius=6)
            draw_text(surf, 'S', self.rect.x+8, self.rect.y+4, color=BLACK, size=22)
        elif self.ptype == 'magnet':
            pygame.draw.rect(surf, (255,215,90), self.rect, border_radius=6)
            draw_text(surf, 'M', self.rect.x+8, self.rect.y+4, color=BLACK, size=22)
        elif self.ptype == 'turbo':
            pygame.draw.rect(surf, (150,255,150), self.rect, border_radius=6)
            draw_text(surf, 'T', self.rect.x+8, self.rect.y+4, color=BLACK, size=22)


class Coin:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.rect = pygame.Rect(x, y, 14, 14)

    def update(self, dt):
        self.x -= self.speed * dt
        self.rect.x = int(self.x)

    def draw(self, surf):
        pygame.draw.circle(surf, (255, 215, 0), (self.rect.centerx, self.rect.centery), 7)


# Game state
player = Player()
obstacles = deque()
powerups = deque()
coins = deque()
scroll_speed = INITIAL_SCROLL_SPEED
score = 0
running = True
paused = False

# Day/Night cycle
cycle_len = 20000  # ms for a full day-night cycle
start_time = pygame.time.get_ticks()

# Background layers (simple parallax rectangles)
clouds = [{'x': random.randint(0, WIDTH), 'y': random.randint(20, 120), 'w': random.randint(80, 180), 'speed': 0.2} for _ in range(8)]

# Helper for collisions and pickups

def spawn_obstacle(speed):
    kind = random.choice(['drone', 'laser'])
    if kind == 'drone':
        h = random.randint(28, 48)
        w = random.randint(48, 76)
        y = GROUND_Y - h - random.randint(0, 40)
    else:
        # laser gate
        h = random.randint(64, 140)
        w = 18
        y = GROUND_Y - h
    x = WIDTH + 50
    obstacles.append(Obstacle(kind, x, y, w, h, speed))


def spawn_powerup(speed):
    p = random.choice(['shield', 'magnet', 'turbo'])
    x = WIDTH + 40
    y = random.randint(GROUND_Y - 200, GROUND_Y - 80)
    powerups.append(Powerup(p, x, y, speed))


def spawn_coin(speed):
    x = WIDTH + 40
    y = random.randint(GROUND_Y - 140, GROUND_Y - 40)
    coins.append(Coin(x, y, speed))


# Main loop
last_time = pygame.time.get_ticks()

while running:
    now = pygame.time.get_ticks()
    dt_ms = clock.tick(FPS)
    dt = dt_ms / 16.6667  # normalized to ~60fps

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key in (pygame.K_SPACE, pygame.K_w, pygame.K_UP):
                player.jump()
            if event.key in (pygame.K_LSHIFT, pygame.K_RSHIFT):
                player.start_dash(now)
            if event.key in (pygame.K_DOWN, pygame.K_s):
                player.duck(True)
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_DOWN, pygame.K_s):
                player.duck(False)
        elif event.type == SPAWN_OBSTACLE:
            spawn_obstacle(scroll_speed)
        elif event.type == SPAWN_POWERUP:
            spawn_powerup(scroll_speed)
        elif event.type == SPAWN_COIN:
            spawn_coin(scroll_speed)

    # speed scaling
    scroll_speed += SPEED_INCREASE_RATE * dt_ms
    active_speed = scroll_speed * (DASH_MULT if player.dashing or player.turbo else 1.0)

    # update player
    player.update(dt, now)

    # update obstacles/powerups/coins
    for o in list(obstacles):
        o.update(dt * active_speed)
        if o.rect.right < -50:
            obstacles.popleft()
    for p in list(powerups):
        p.update(dt * scroll_speed)
        if p.rect.right < -50:
            powerups.popleft()
    for c in list(coins):
        c.update(dt * scroll_speed)
        if c.rect.right < -50:
            coins.popleft()

    # Magnet effect: pull nearby coins
    if player.magnet:
        for c in coins:
            if abs(c.rect.centerx - player.x) < 200 and abs(c.rect.centery - player.y) < 120:
                # simple attraction
                c.x -= (c.x - (player.x + player.w)) * 0.12
                c.rect.x = int(c.x)

    # Collisions
    pre_count = len(coins)
    for c in list(coins):
        if player.rect().colliderect(c.rect):
            coins.remove(c)
            player.score += 10 * (2 if player.turbo else 1)
    # powerups
    for p in list(powerups):
        if player.rect().colliderect(p.rect):
            powerups.remove(p)
            if p.ptype == 'shield':
                player.shield = True
                player.shield_end = now + SHIELD_DURATION
            elif p.ptype == 'magnet':
                player.magnet = True
                player.magnet_end = now + MAGNET_DURATION
            elif p.ptype == 'turbo':
                player.turbo = True
                player.turbo_end = now + TURBO_DURATION

    # obstacle collisions
    dead = False
    for o in list(obstacles):
        if player.rect().colliderect(o.rect):
            if player.shield:
                obstacles.remove(o)
                player.shield = False
            else:
                dead = True
                break

    if dead:
        # Game over screen
        screen.fill((20, 20, 20))
        draw_text(screen, 'GAME OVER', WIDTH//2 - 80, HEIGHT//2 - 40, color=WHITE, size=48)
        draw_text(screen, f'Score: {player.score}', WIDTH//2 - 60, HEIGHT//2 + 10, color=WHITE, size=36)
        draw_text(screen, 'Press R to restart or ESC to quit', WIDTH//2 - 160, HEIGHT//2 + 60, color=WHITE, size=22)
        pygame.display.flip()
        # wait for restart or quit
        waiting = True
        while waiting:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    waiting = False
                    running = False
                elif ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_r:
                        # reset everything
                        player = Player()
                        obstacles.clear()
                        powerups.clear()
                        coins.clear()
                        scroll_speed = INITIAL_SCROLL_SPEED
                        player.score = 0
                        waiting = False
                    elif ev.key == pygame.K_ESCAPE:
                        waiting = False
                        running = False
            clock.tick(30)
        continue

    # incremental score by distance
    player.score += int(scroll_speed * 0.05 * dt_ms)

    # draw background (day/night blend)
    cycle_pos = ((now - start_time) % cycle_len) / cycle_len
    # cycle_pos 0..1 where 0..0.5 is day -> night transition
    t = (math.sin(cycle_pos * math.pi * 2) + 1) / 2
    sky_r = SKY_DAY[0] * t + SKY_NIGHT[0] * (1 - t)
    sky_g = SKY_DAY[1] * t + SKY_NIGHT[1] * (1 - t)
    sky_b = SKY_DAY[2] * t + SKY_NIGHT[2] * (1 - t)
    screen.fill((int(sky_r), int(sky_g), int(sky_b)))

    # parallax clouds
    for cl in clouds:
        cl['x'] -= cl['speed'] * scroll_speed * 0.6
        if cl['x'] < -200:
            cl['x'] = WIDTH + random.randint(20, 200)
            cl['y'] = random.randint(20, 120)
            cl['w'] = random.randint(80, 180)
        pygame.draw.ellipse(screen, (255,255,255,40), (int(cl['x']), cl['y'], cl['w'], 40))

    # ground
    pygame.draw.rect(screen, GROUND_COLOR, (0, GROUND_Y, WIDTH, HEIGHT - GROUND_Y))

    # draw coins
    for c in coins:
        c.draw(screen)

    # draw powerups
    for p in powerups:
        p.draw(screen)

    # draw obstacles
    for o in obstacles:
        o.draw(screen)

    # draw player
    player.draw(screen, now)

    # HUD
    draw_text(screen, f'Score: {player.score}', 14, 10)
    draw_text(screen, f'Speed: {scroll_speed:.1f}', 14, 36)
    # active powerups
    pu_texts = []
    if player.shield:
        pu_texts.append('Shield')
    if player.magnet:
        pu_texts.append('Magnet')
    if player.turbo:
        pu_texts.append('Turbo')
    draw_text(screen, ' | '.join(pu_texts), WIDTH - 220, 10)

    pygame.display.flip()

pygame.quit()
sys.exit()
