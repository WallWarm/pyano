import pygame
import display as d
from pygame import mixer


pygame.init()
pygame.mixer.init()
width = 1500
height = 720
screen = pygame.display.set_mode([width,height])
pygame.display.set_caption('PYANO')

run = True
while run:
    screen.fill('gray')
    d.disp()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.display.flip()
pygame.quit()

 