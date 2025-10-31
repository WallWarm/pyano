import pygame
import notes as n
from pygame import mixer

pygame.init()
pygame.mixer.init()

wbsounds = [
        pygame.K_z,
        pygame.K_x,
        pygame.K_c,
        pygame.K_v,
        pygame.K_b,
        pygame.K_n,
        pygame.K_m,
        pygame.K_q,
        pygame.K_w,
        pygame.K_e,
        pygame.K_r,
        pygame.K_t,
        pygame.K_y,
        pygame.K_u,
        pygame.K_i,
        pygame.K_o,
        pygame.K_p,
        pygame.K_LEFTBRACKET,
        pygame.K_RIGHTBRACKET,
        pygame.KSCAN_APOSTROPHE,
        pygame.K_SLASH,
        pygame.KSCAN_GRAVE,
    ]

bbsounds = [
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

dwbsounds = dict.fromkeys(wbsounds)
dwbsounds = {key: i for (i, key) in enumerate(dwbsounds, 0)}
dbbsounds = dict.fromkeys(bbsounds)
dbbsounds = {key: i for (i, key) in enumerate(dbbsounds, 0)}

def play():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            wnote = n.whitenotes[dwbsounds.get(event.key)]
            bnote = n.blacknotes[dbbsounds.get(event.key)]
            if wnote is not None:
                note = pygame.mixer.Sound(str(wnote)+'.mp3')
                note.play()
            if bnote is not None:
                note = pygame.mixer.Sound(str(bnote)+'.mp3')
                note.play()


