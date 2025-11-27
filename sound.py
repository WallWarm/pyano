import pygame
import notes as n
import display as d

pygame.mixer.init()

pressed_last_frame = set()

white_sounds = {
    key: pygame.mixer.Sound(n.whitenotes[i] + ".mp3")
    for i, key in enumerate(d.wbkeys)
}

black_sounds = {
    key: pygame.mixer.Sound(n.blacknotes[i] + ".mp3")
    for i, key in enumerate(d.bbkeys)
}


def play():
    global pressed_last_frame

    keys = pygame.key.get_pressed()

    current_pressed = {k for k in d.wbkeys if keys[k]}
    current_pressed |= {k for k in d.bbkeys if keys[k]}

    new_presses = current_pressed - pressed_last_frame

    for key in new_presses:
        if key in white_sounds:
            white_sounds[key].play()
        elif key in black_sounds:
            black_sounds[key].play()

    pressed_last_frame = current_pressed
    