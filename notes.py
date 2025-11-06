import display as d
import pygame
height = 720
w3 = 'C3 D3 E3 F3 G3 A3 B3 '
w4 = w3.replace('3','4')
w5 = w3.replace('3','5')
w = w3 + w4 + w5 +'C6'
whitenotes = w.split()

b3 = 'Db3 Eb3 Gb3 Ab3 Bb3 '
b4 = b3.replace('3','4')
b5 = b3.replace('3','5')
b = b3 + b4 + b5
blacknotes = b.split()

k3 = 'Z S X D C V G B H N J M'
k4 = 'Q 2 W 3 E R 5 T 6 Y 7 U'
k5 = "I 9 O 0 P [ = ] ; ' > /"
octave3 = k3.split()
octave4 = k4.split() 
octave5 = k5.split()
fullboard = octave3 + octave4 + octave5 +['`']

allwhites = "Z X C V B N M Q W E R T Y U I O P [ ] ' / `"
allblacks = "S D G H J 2 3 5 6 7 9 0 = ; > "
wboard = allwhites.split()
bboard = allblacks.split()

all3 = 'C3 C#3 D3 D#3 E3 F3 F#3 G3 G#3 A3 A#3 B3 '
all4 = all3.replace('3', '4')
all5 = all3.replace('3', '5')
a = all3 + all4 + all5 + 'C6'
allnotes = a.split()

#allnotes - all the individual piano notes in order
#fullbaord - all the individual keyboard notes in order

#wboard - all white notes on keyboard
#bboard - all black notesonkeyboard

#whitenotes - all white piano notes
#blacknotes - all black piano notes

#wboard = whitenotes = 22
#bboard = blacknotes = 15
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
dbbkeys = {key: [175 + ((i) * 50), height - 400, 40, 200] for (i, key) in enumerate(dbbkeys, 1)}
print(dbbkeys)
