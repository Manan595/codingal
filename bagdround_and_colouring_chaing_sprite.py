import pygame
import random
pygame.init()
SPRITE_COLOUR_CHANGE_EVENT= pygame.USEREVENT + 1
BAGROUND_COLOUR_CHANGE_EVENT= pygame.USEREVENT + 2 
BLUE = pygame.Color('blue')
LIGHTBLUE=pygame.Color ('lighblue')
DARKBLUE= pygame.Color( 'darkblue')

YELLOW= pygame.Color('yellow')
MAGENTA= pygame.Color('magenta')
ORANGE= pygame.Color('orange')
WHITE= pygame.Color('white')

class Sprite(pygame.sprite.Sprite):

    def __init__(self,color,height,width):
        super().__init__()
        self.image = pygame.SURface([width,height])
        self. image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1,1]),random.choice([-1,1])]
    def updat(self):
        self.rect.move_ip(self.velocity)
        boundary_hit= True

        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0]= -self.veocity[1]
            boundary_hit= True

        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOUR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BAGROUND_COLOUR_CHANGE_EVENT))
    def change_colour(self):
        self.image.fill(random.choice9([YELLOW,MAGENTA,ORANGE,WHITE]))



def change_baground_colour():
    global bg_colour
    bg_colour= random.choice[(BLUE,DARKBLUE,LIGHTBLUE)]


all_sprites_list= pygame.sprite.Group()
sp1= Sprite(WHITE,20, 30)
sp1.rect.x=random.radient(0,480)
sp1.rect.y=random.radient(0,370)
all_sprites_list.add(sp1)
screen= pygame.display.set_mode((500,400))
pygame.display.set_caption('colourfull bounce')

bg_colour=BLUE