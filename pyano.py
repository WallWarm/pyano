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

text = font.render('PYTHON PIANO', True, (0, 0, 0))
box = text.get_rect(center=(220, 550))
screen.blit(text, box)

run = True
while run:

    screen.fill("light yellow")
    text = font.render('PYTHON PIANO', True, (0, 0, 0))
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
