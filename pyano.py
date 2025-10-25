import pygame
import notes as n
from pygame import mixer

pygame.init()
width = 1500
height = 720
screen = pygame.display.set_mode([width,height])
pygame.display.set_caption('PYANO')
wfont = pygame.font.SysFont('times new roman',24)
bfont = pygame.font.SysFont('times new roman',20)
def disp():
    white = []
    shift=0
    for i in range(len(n.whitenotes)):
        wkey = pygame.draw.rect(screen,'white',[150+((i+1)*50),height-400,50,300],0,4)
        pygame.draw.rect(screen,'black',[150+((i+1)*50),height-400,50,300],2,4)
        white.append(wkey)

        text = wfont.render(n.whitenotes[i],True, (225,0,0))
        box = text.get_rect(center=(225+shift,545))
        screen.blit(text,box)

        text = wfont.render(n.wboard[i],True, (0,0,0))
        box = text.get_rect(center=(225+shift,580))
        screen.blit(text,box)
        shift+=50

    black = []
    for i in (0,1,3,4,5,7,8,10,11,12,14,15,17,18,19,21):
        b = n.blacknotes
        bkey = pygame.draw.rect(screen,'black',[180+((i+1)*50),height-400,40,200],0,4)
        pygame.draw.rect(screen,'black',[(i+1)*50,height-400,50,300],2,4)
        black.append(bkey)
            
'''
def writeblack():
    shift = 0
    for i in range(21):
        if i in [2,6,9,13,16,20]:
            shift+=50
        else:
            text = bfont.render(n.blacknotes[i],True, (255,255,255))
            box = text.get_rect(center=(296+shift,345))
            screen.blit(text,box)
            shift+=50
            shift+=50
'''
text = bfont.render('',True, (255,255,255))
box = text.get_rect(center=(250,450))

run = True
while run:
    screen.fill('black')
    disp()
    screen.blit(text,box)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()

 