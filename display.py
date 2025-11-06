import pygame

import notes as n



width = 1500

height = 720

wfont = pygame.font.SysFont("times new roman", 24)

bfont = pygame.font.SysFont("times new roman", 20)

screen = pygame.display.set_mode([width, height])





def disp():

    shift = 0

    for i in range(len(n.whitenotes)):

        wkey = pygame.draw.rect(

            screen, "white", [145 + ((i + 1) * 50), height - 400, 50, 300], 0, 4

        )

        pygame.draw.rect(

            screen, "black", [145 + ((i + 1) * 50), height - 400, 50, 300], 2, 4

        )



        text = wfont.render(n.whitenotes[i], True, (0, 0, 0))

        box = text.get_rect(center=(220 + shift, 550))

        screen.blit(text, box)



        text = wfont.render(n.wboard[i], True, (225, 0, 0))

        box = text.get_rect(center=(220 + shift, 585))

        screen.blit(text, box)

        shift += 50



    j = 0

    for i in (0, 1, 3, 4, 5, 7, 8, 10, 11, 12, 14, 15, 17, 18, 19):

        bkey = pygame.draw.rect(screen, "black", [175 + ((i + 1) * 50), height - 400, 40, 200], 0, 4)



        text = bfont.render(n.blacknotes[j], True, (255, 255, 255))

        box = text.get_rect(center=(195 + (i + 1) * 50, 470))

        screen.blit(text, box)



        text = bfont.render(n.bboard[j], True, (255, 0, 0))

        box = text.get_rect(center=(195 + (i + 1) * 50, 495))

        screen.blit(text, box)

        j += 1



wbkeys = [

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



dwbkeys = dict.fromkeys(wbkeys)

dwbkeys = {key: [145 + ((i) * 50), height - 200, 50, 100] for (i, key) in enumerate(dwbkeys, 1)}

dbbkeys = dict.fromkeys(bbkeys)







(1, 2, 4, 5, 6, 8, 9, 11, 12, 13, 15, 16, 18, 19, 20)





dbbkeys = {115: [225, 320, 40, 200], 
            100: [275, 320, 40, 200], 
            103: [375, 320, 40, 200], 
            104: [425, 320, 40, 200], 
            106: [475, 320, 40, 200], 
            50: [575, 320, 40, 200], 
            51: [625, 320, 40, 200], 
            53: [725, 320, 40, 200], 
            54: [775, 320, 40, 200], 
            55: [825, 320, 40, 200], 
            57: [925, 320, 40, 200], 
            48: [975, 320, 40, 200], 
            61: [1075, 320, 40, 200],
            59: [1125, 320, 40, 200],
            62: [1175, 320, 40, 200]
        }







def hiplay():
    for event in pygame.event.get():
        for x in dwbkeys.keys():
            keys = pygame.key.get_pressed()
            if keys[x]:
                pygame.draw.rect(
                    screen, "green", dwbkeys.get(x), 2, 4
                )
                wnote = n.whitenotes[wbkeys.index(x)]
                note = pygame.mixer.Sound(str(wnote)+'.mp3')
                if event.type==pygame.KEYDOWN:
                    note.play()
                if event.type==pygame.KEYUP:
                    note.stop()
        for y in dbbkeys.keys():
            keys = pygame.key.get_pressed()
            if keys[y]:
                pygame.draw.rect(
                    screen, "green", dbbkeys.get(y), 2, 4
                )
                bnote = n.blacknotes[bbkeys.index(y)]
                note = pygame.mixer.Sound(str(bnote)+'.mp3')
                if event.type==pygame.KEYDOWN:
                    note.play()
                if event.type==pygame.KEYUP:
                    note.stop()