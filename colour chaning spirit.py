import pygame
def main():
    pygame.init()
screen_width, screen_height= 500,500
scree=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('colour chaning spirit')

colours={'red':pygame.colour('red'),'green':pygame.colour('green'),'blue':pygame.colour('blue'),'yellow':pygame.colour('yellow'),'white':pygame.colour('white'),}
current_colout= colours ['white']

x,y = 30,30
sprite_width,sprite_height=60,60
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
pressed= pygame.key.get_pressed()
if pressed [ pygame.K_Left]:x -= 3 
if pressed [ pygame.K_RIGHT]:x += 3 
if pressed [ pygame.K_UP]:y -= 3 
if pressed [ pygame.K_DOWN]:y += 3 

x= min(max(0,x),screen_height)