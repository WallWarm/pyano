import pygame
import display as d
import sound as s


pygame.init()
pygame.mixer.init()

width = 1500
height = 720
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("Python Piano")

font = pygame.font.SysFont("times new roman", 120)


run = True
while run:

    screen.fill((117,8,81))
    text = font.render('PYTHON PIANO', True, (225, 225, 225))
    box = text.get_rect(center=(750, 200))
    screen.blit(text, box)
    d.disp()
    d.highlight()
    s.play()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()
