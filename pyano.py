import pygame
import display as d
import sound as s


pygame.init()
pygame.mixer.init()
icon = pygame.image.load('finalicon.png')
pygame.display.set_icon(icon)
width = 1500
height = 720
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("PYANO")

font = pygame.font.SysFont("times new roman", 120)
smallfont = pygame.font.SysFont("times new roman", 40)
reallysmallfont = pygame.font.SysFont("times new roman", 20)
run = True
while run:

    screen.fill((75,11,51))
    text = font.render('PYANO', True, (225, 225, 225))
    box = text.get_rect(center=(750, 150))
    screen.blit(text, box)
    text1 = smallfont.render('37 notes || 3 octaves', True, (225, 225, 225))
    box1 = text1.get_rect(center=(750, 250))
    screen.blit(text1, box1)
    text1 = reallysmallfont.render('created by Arnav Guntur, XIIC', True, (225, 225, 225))
    box1 = text1.get_rect(center=(750, 680))
    screen.blit(text1, box1)
    d.disp()
    d.highlight()
    s.play()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PERIOD:
                print (ascii(event.key))
pygame.quit()
