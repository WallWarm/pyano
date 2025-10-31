import pygame
from pygame import mixer


pygame.init()
import display as d
pygame.mixer.init()
import sounds as s
width = 1500
height = 720
screen = pygame.display.set_mode([width,height])
pygame.display.set_caption('PYANO')

bbkeys = [
        pygame.K_s,
        pygame.K_d,
        pygame.K_g,
        pygame.K_h,
        pygame.K_j,
        pygame.K_2,
        pygame.K_3,
        pygame.K_5,
        pygame.K_6,
        pygame.K_7,
        pygame.K_9,
        pygame.K_0,
        pygame.K_EQUALS,
        pygame.K_SEMICOLON,
        pygame.K_GREATER,
    ]

dbbkeys = dict.fromkeys(bbkeys)
dbbkeys = {115: [225, 320, 40, 200], 100: [275, 320, 40, 200], 103: [325, 320, 40, 200], 104: [375, 320, 40, 200], 106: [425, 320, 40, 200], 50: [475, 320, 40, 200], 51: [525, 320, 40, 200], 53: [575, 320, 40, 200], 54: [625, 320, 40, 200], 55: [675, 320, 40, 200], 57: [725, 320, 40, 200], 48: [775, 320, 40, 200], 61: [825, 320, 40, 200], 59: [875, 320, 40, 200], 62: [925, 320, 40, 200]}
run = True
dbbkeys = {key: [175 + ((i) * 50), height - 400, 40, 200] for (i, key) in enumerate(dbbkeys, (0, 1, 3, 4, 5, 7, 8, 10, 11, 12, 14, 15, 17, 18, 19))}
print(dbbkeys)

while run:
    screen.fill('gray')
    d.disp()
    d.highlight()
    s.play()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.display.flip()
pygame.quit()
print(d.dwbkeys)
 