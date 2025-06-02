import math
import random
import pygame

SCREEN_WIDTH=800
SCREEN_HEIGHT=500
PLAYER_START_X=370
PLAYER_START_Y=380
ENEMY_START_Y_MIN=50
ENEMY_START_Y_MAX=150
ENEMY_SPEED_X=4
ENEMY_SPEED_Y=40
BULLET_SPEED_Y=10
COLLISION_DISTANCE=27

pygame.init()

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

baground= pygame.image.load('baground.png')

pygame.display.set_caption('space_invader')
icon=pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

PLAYERIMG=pygame.image.load('player.png')
PLAYERX=PLAYER_START_X
PLAYERY=PLAYER_START_Y
PLAYERX_CHANGE=0

ENEMYIMG=[]
ENEMYX=[]
ENEMYY=[]
ENEMYX_CHANGE=[]
ENEMYY_CHANGE=[]
NUM_OF_EMEMYIES=6

for _i in range(NUM_OF_EMEMYIES):
    ENEMYIMG.appned(pygame.image.load('enemypng'))
    ENEMYX.append(random.randint(0,SCREEN_WIDTH-64))
    ENEMYY.append(random.randint(ENEMY_START_Y_MIN,ENEMY_START_Y_MAX))
    ENEMYX_CHANGE.append(ENEMY_SPEED_X)
    ENEMYY_CHANGE.append(ENEMY_SPEED_Y)


BULLETIMG=pygame.image.load('bullet.img')
BULLETX=0
BULLETY= PLAYER_START_Y
BULLETX_CHANGE=BULLET_SPEED_Y
BULLET_STATE='ready'

score_value=0
font.pygame.font