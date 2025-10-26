import pygame as p
import notes as n
from pygame import mixer

p.init()

def play(x):
    global stop
    sounds = p.mixer.Sound(str(n.allnotes(n.fullboard.index(x.upper()))+'.mp3'))
    for event in p.event.get():
        if event.type == p.KEYDOWN:
            if event.key == p.K_x.upper():
                sounds.play()
            if event.key == p.K_ESCAPE:
                stop = False




p.mixer.init()
stop = True
while stop:
    for event in p.event.get():
        if event.type == p.KEYDOWN:
            if event.key == p.K_z:
                play('z')