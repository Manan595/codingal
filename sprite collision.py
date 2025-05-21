import pygame
import random

SCREEN_WIDTH,SCREEN_HEIGHT=500,400
movement_speed=5
font_size=72

pygame.init()

baground_image = pygame.transform.scale(pygame.image.load("image add it ")
                                        (SCREEN_HEIGHT,SCREEN_WIDTH))

font = pygame.font.SysFont('Times New Roman',font_size)

class sprite(pygame.sprite.Sprite):
    def __init__ (self,color,height,width):
     super().__init__()
     self.image= pygame.Surface([width,height])
     self.image.fill(pygame.Color('dogerblue'))
     pygame.draw.rect(self.image,color,pygame.rect)
     self.rect= self.image.get_rect()

    def move(self, x_change,y_change):
       self.rect.x=max(
          min(self.rect.x+x_change,SCREEN_WIDTH - self.rect.width), 0)
       self.rect.y=max(
          min(self.rect.y+ y_change,SCREEN_HEIGHT- self.rect.height),0)
       
screen= pygame.display.set_mode((SCREEN_WIDTH,SCREEN_WIDTH))
pygame.display.set_caption('sprite collosion')
all_sprites = pygame.sprite.Group()

sprite1= sprite(pygame.Color('black'),20,30)
sprite1.rect.x,sprite1.rect.y= random.randint(
     0,SCREEN_WIDTH - sprite1.rect.width),random.randint