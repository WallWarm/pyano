w3 = 'C3 D3 E3 F3 G3 A3 B3 '
w4 = w3.replace('3', '4')
w5 = w3.replace('3', '5')
whitenotes = (w3 + w4 + w5 + 'C6').split()

b3 = 'Db3 Eb3 Gb3 Ab3 Bb3 '
b4 = b3.replace('3', '4')
b5 = b3.replace('3', '5')
blacknotes = (b3 + b4 + b5).split()

wboard = "Z X C V B N M Q W E R T Y U I O P [ ] ' / `".split()
bboard = "S D G H J 2 3 5 6 7 9 0 = ; .".split()
