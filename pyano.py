import pygame
from pygame import mixer


pygame.init()
import display as d
pygame.mixer.init()
width = 1500
height = 720
screen = pygame.display.set_mode([width,height])
pygame.display.set_caption('PYANO')


run = True
while run:
    screen.fill('gray')
    d.disp()
    d.hiplay()
    pygame.display.update()
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.display.flip()
pygame.quit()
print(d.dwbkeys)
 