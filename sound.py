import pygame
from pygame import mixer

import display as d
import notes as n


def play():
    for x in d.dwbkeys.keys():
        keys = pygame.key.get_pressed()
        if keys[x]:
            note = pygame.mixer.Sound(n.whitenotes[d.wbkeys.index(x)] + ".mp3")
            note.play(maxtime=300)
    for y in d.dbbkeys.keys():
        keys = pygame.key.get_pressed()
        if keys[y]:
            note = pygame.mixer.Sound(n.blacknotes[d.bbkeys.index(y)] + ".mp3")
            note.play(maxtime=300)
