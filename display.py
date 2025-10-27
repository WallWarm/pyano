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

        text = wfont.render(n.whitenotes[i], True, (225, 0, 0))
        box = text.get_rect(center=(220 + shift, 550))
        screen.blit(text, box)

        text = wfont.render(n.wboard[i], True, (0, 0, 0))
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


def highlight():
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
    dwbkeys = {key: [145 + ((i) * 50), height - 400, 50, 300] for (i, key) in enumerate(dwbkeys, 1)}
    dbbkeys = dict.fromkeys(bbkeys)
    dbbkeys = {key: [145 + ((i) * 50), height - 400, 50, 300] for (i, key) in enumerate(dbbkeys, 1)}
    def highlight():
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                wcoords = dwbkeys.get(event.key)
                bcoords = dbbkeys.get(event.key)
                if wcoords is not None:
                    pygame.draw.rect(screen, "green", wcoords, 2, 4)
                if bcoords is not None:
                    pygame.draw.rect(screen, "green", bcoords, 2, 4)
