import pygame
pygame.init()
white= (225,255,255 )

clock = pygame.time.Clock()
display_surface=pygame.display.set_mode((500, 500))
pygame.display.set_caption('image')
image= pygame.image.load('sungjinwoo.jpeg')

DEFAULT_IMAGE_SIZE = (200, 200)
image= pygame.transform.scale(image,DEFAULT_IMAGE_SIZE)

while True:
    display_surface.fill(white)
    display_surface.blit(image, DEFAULT_IMAGE_SIZE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.flip()