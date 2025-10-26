import pygame
import notes as n

width = 1500
height = 720
wfont = pygame.font.SysFont('times new roman',24)
bfont = pygame.font.SysFont('times new roman',20)
screen = pygame.display.set_mode([width,height])

def disp():
    shift=0
    for i in range(len(n.whitenotes)):
        wkey = pygame.draw.rect(screen,'white',[145+((i+1)*50),height-400,50,300],0,4)
        pygame.draw.rect(screen,'black',[145+((i+1)*50),height-400,50,300],2,4)

        text = wfont.render(n.whitenotes[i],True, (225,0,0))
        box = text.get_rect(center=(220+shift,550))
        screen.blit(text,box)

        text = wfont.render(n.wboard[i],True, (0,0,0))
        box = text.get_rect(center=(220+shift,585))
        screen.blit(text,box)
        shift+=50
        
    j=0
    for i in (0,1,3,4,5,7,8,10,11,12,14,15,17,18,19):
        bkey = pygame.draw.rect(screen,'black',[175+((i+1)*50),height-400,40,200],0,4)

        text = bfont.render(n.blacknotes[j],True, (255,255,255))
        box = text.get_rect(center=(195+(i+1)*50,470))
        screen.blit(text,box)

        text = bfont.render(n.bboard[j],True, (255,0,0))
        box = text.get_rect(center=(195+(i+1)*50,495))
        screen.blit(text,box)
        j+=1