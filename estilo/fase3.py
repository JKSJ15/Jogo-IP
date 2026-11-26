import pygame

from constantes import NATIVE_W, NATIVE_H


# Superfície interna de 320 x 240
canvas = pygame.Surface((NATIVE_W, NATIVE_H))
DOOR_RECT = pygame.Rect(315, 110, 5, 34)


# PALETA DE CORES
C_BG_VOID       = (40, 46, 56)
C_WALL_TOP      = (140, 148, 136)
C_WALL_MAIN     = (168, 174, 152)
C_WALL_BASE     = (104, 112, 116)
C_OUTLINE       = (44, 48, 56)

C_FLOOR_WHITE_1 = (244, 246, 248)
C_FLOOR_WHITE_2 = (232, 236, 240)
C_FLOOR_LINE    = (204, 210, 218)
C_FLOOR_SHADOW  = (184, 190, 200)

C_DESK_TOP      = (248, 250, 252)
C_DESK_EDGE     = (140, 148, 160)
C_DESK_LEG      = (88, 96, 108)

C_CHAIR_ORANGE  = (224, 136, 64)
C_CHAIR_SHADE   = (184, 100, 40)
C_CHAIR_LIGHT   = (244, 168, 96)

C_PROF_WOOD_1   = (148, 96, 76)
C_PROF_WOOD_2   = (112, 70, 56)

C_PROJ_BODY     = (168, 176, 192)
C_PROJ_SHADE    = (112, 120, 136)
C_PROJ_LENS     = (56, 64, 80)

# SALA
def draw_room(surf):
    surf.fill(C_BG_VOID)

    room_x, room_y = 0, 0
    room_w, room_h = NATIVE_W, NATIVE_H
    wall_h = 48
    floor_y = room_y + wall_h
    floor_h = room_h - wall_h

    # Piso
    pygame.draw.rect(
        surf, C_FLOOR_WHITE_1,
        (room_x, floor_y, room_w, floor_h)
    )

    plank_h = 10
    plank_w = 48

    for y in range(floor_y, floor_y + floor_h, plank_h):
        row = (y - floor_y) // plank_h
        offset = (plank_w // 2) if row % 2 == 1 else 0

        pygame.draw.line(
            surf, C_FLOOR_LINE,
            (room_x, y),
            (room_x + room_w - 1, y)
        )

        for x in range(room_x + offset, room_x + room_w, plank_w):
            if (x // plank_w + row) % 2 == 0:
                w = min(plank_w, room_x + room_w - x)
                h = min(plank_h - 1, floor_y + floor_h - y - 1)

                if h > 0:
                    pygame.draw.rect(
                        surf, C_FLOOR_WHITE_2,
                        (x, y + 1, w, h)
                    )

            pygame.draw.line(
                surf, C_FLOOR_LINE,
                (x, y),
                (x, min(y + plank_h, floor_y + floor_h - 1))
            )

    # Sombra da parede
    pygame.draw.rect(
        surf, C_FLOOR_SHADOW,
        (room_x, floor_y, room_w, 3)
    )

    # Paredes
    pygame.draw.rect(
        surf, C_WALL_TOP,
        (room_x, room_y, room_w, 5)
    )

    pygame.draw.rect(
        surf, C_WALL_MAIN,
        (room_x, room_y + 5, room_w, wall_h - 9)
    )

    pygame.draw.rect(
        surf, C_WALL_BASE,
        (room_x, floor_y - 4, room_w, 4)
    )

    # Moldura externa
    pygame.draw.rect(
        surf, C_OUTLINE,
        (room_x - 1, room_y - 1, room_w + 2, room_h + 2),
        1
    )

    pygame.draw.line(
        surf, C_OUTLINE,
        (room_x, floor_y),
        (room_x + room_w - 1, floor_y)
    )

    # Porta
    door_x = room_x + room_w - 5
    door_y = floor_y + 62

    pygame.draw.rect(
        surf, (156, 104, 64),
        (door_x, door_y, 5, 34)
    )

    pygame.draw.rect(
        surf, C_OUTLINE,
        (door_x, door_y, 5, 34), 1
    )


# LOUSA DIGITAL E PROJETORES
def draw_smartboard_and_projectors(surf, center_x, top_y):

    bw, bh = 86, 26
    bx = center_x - bw // 2
    by = top_y

    # Lousa
    pygame.draw.rect(
        surf, (136, 144, 164),
        (bx, by, bw, bh)
    )

    pygame.draw.rect(
        surf, C_OUTLINE,
        (bx, by, bw, bh), 1
    )

    pygame.draw.line(
        surf, C_OUTLINE,
        (bx + 7, by),
        (bx + 7, by + bh - 1)
    )

    pygame.draw.line(
        surf, C_OUTLINE,
        (bx + bw - 8, by),
        (bx + bw - 8, by + bh - 1)
    )

    pygame.draw.rect(
        surf, (184, 216, 232),
        (bx + 9, by + 3, bw - 18, bh - 6)
    )

    pygame.draw.rect(
        surf, C_OUTLINE,
        (bx + 9, by + 3, bw - 18, bh - 6), 1
    )

    pygame.draw.polygon(
        surf, (216, 236, 248),
        [
            (bx + 14, by + 4),
            (bx + 24, by + 4),
            (bx + 15, by + bh - 5),
            (bx + 10, by + bh - 5)
        ]
    )

    pygame.draw.rect(
        surf, (136, 144, 164),
        (center_x - 16, by + bh, 32, 3)
    )

    pygame.draw.rect(
        surf, C_OUTLINE,
        (center_x - 16, by + bh, 32, 3), 1
    )

    # Projetores
    for px in [bx - 24, bx + bw + 8]:

        py = top_y - 2

        pygame.draw.rect(
            surf, C_PROJ_BODY,
            (px + 2, py, 12, 5)
        )

        pygame.draw.rect(
            surf, C_OUTLINE,
            (px + 2, py, 12, 5), 1
        )

        pygame.draw.rect(
            surf, C_PROJ_SHADE,
            (px + 6, py + 5, 4, 8)
        )

        pygame.draw.rect(
            surf, C_OUTLINE,
            (px + 6, py + 5, 4, 8), 1
        )

        pygame.draw.rect(
            surf, C_PROJ_BODY,
            (px, py + 13, 16, 11)
        )

        pygame.draw.rect(
            surf, C_PROJ_SHADE,
            (px, py + 20, 16, 4)
        )

        pygame.draw.rect(
            surf, C_OUTLINE,
            (px, py + 13, 16, 11), 1
        )

        pygame.draw.rect(
            surf, C_PROJ_LENS,
            (px + 2, py + 18, 5, 5)
        )

        pygame.draw.rect(
            surf, (160, 200, 230),
            (px + 3, py + 19, 2, 2)
        )


# OBJETOS DA SALA
def draw_classroom_props(surf):

    # Mesa do professor
    px, py = 28, 52

    pygame.draw.rect(
        surf, C_PROF_WOOD_1,
        (px + 18, py - 12, 12, 12)
    )

    pygame.draw.rect(
        surf, C_OUTLINE,
        (px + 18, py - 12, 12, 12), 1
    )

    pygame.draw.rect(
        surf, C_FLOOR_SHADOW,
        (px + 1, py + 20, 48, 3)
    )

    pygame.draw.rect(
        surf, C_PROF_WOOD_1,
        (px, py, 48, 14)
    )

    pygame.draw.rect(
        surf, C_PROF_WOOD_2,
        (px, py + 14, 48, 6)
    )

    pygame.draw.rect(
        surf, C_OUTLINE,
        (px, py, 48, 20), 1
    )

    pygame.draw.line(
        surf, C_OUTLINE,
        (px, py + 14),
        (px + 47, py + 14)
    )

    # Notebook
    pygame.draw.rect(
        surf, (136, 148, 172),
        (px + 18, py + 3, 13, 8)
    )

    pygame.draw.rect(
        surf, C_OUTLINE,
        (px + 18, py + 3, 13, 8), 1
    )

    # Lixeira
    tx, ty = px + 51, py + 7

    pygame.draw.rect(
        surf, (168, 176, 188),
        (tx, ty, 9, 11)
    )

    pygame.draw.rect(
        surf, (96, 104, 116),
        (tx + 2, ty + 1, 5, 3)
    )

    pygame.draw.rect(
        surf, C_OUTLINE,
        (tx, ty, 9, 11), 1
    )

    # Alarme
    ax, ay = 250, 22

    pygame.draw.rect(
        surf, (200, 68, 68),
        (ax, ay, 10, 11)
    )

    pygame.draw.rect(
        surf, (240, 240, 240),
        (ax + 3, ay + 3, 4, 4)
    )

    pygame.draw.rect(
        surf, C_OUTLINE,
        (ax, ay, 10, 11), 1
    )

    # Planta
    vx, vy = 266, 46

    pygame.draw.rect(
        surf, C_FLOOR_SHADOW,
        (vx + 1, vy + 18, 12, 3)
    )

    pygame.draw.rect(
        surf, (168, 152, 112),
        (vx + 2, vy + 10, 10, 8)
    )

    pygame.draw.rect(
        surf, C_OUTLINE,
        (vx + 2, vy + 10, 10, 8), 1
    )

    pygame.draw.ellipse(
        surf, (88, 160, 96),
        (vx, vy, 14, 11)
    )

    pygame.draw.ellipse(
        surf, C_OUTLINE,
        (vx, vy, 14, 11), 1
    )


# CARTEIRAS E CADEIRAS
def draw_student_desk_and_orange_chair(surf, x, y):

    top_w = 16
    bot_w = 24
    h = 12

    p1 = (x - top_w // 2, y)
    p2 = (x + top_w // 2, y)
    p3 = (x + bot_w // 2, y + h)
    p4 = (x - bot_w // 2, y + h)

    # Sombra
    pygame.draw.rect(
        surf, C_FLOOR_SHADOW,
        (p4[0] + 1, p4[1] + 5, bot_w - 1, 5)
    )

    # Pés
    pygame.draw.rect(
        surf, C_DESK_LEG,
        (p4[0] + 1, p4[1] + 2, 3, 6)
    )

    pygame.draw.rect(
        surf, C_OUTLINE,
        (p4[0] + 1, p4[1] + 2, 3, 6), 1
    )

    pygame.draw.rect(
        surf, C_DESK_LEG,
        (p3[0] - 3, p3[1] + 2, 3, 6)
    )

    pygame.draw.rect(
        surf, C_OUTLINE,
        (p3[0] - 3, p3[1] + 2, 3, 6), 1
    )

    # Frente
    pygame.draw.rect(
        surf, C_DESK_EDGE,
        (p4[0], p4[1], bot_w + 1, 3)
    )

    pygame.draw.rect(
        surf, C_OUTLINE,
        (p4[0], p4[1], bot_w + 1, 3), 1
    )

    # Tampo
    pygame.draw.polygon(
        surf, C_DESK_TOP,
        [p1, p2, p3, p4]
    )

    pygame.draw.polygon(
        surf, C_OUTLINE,
        [p1, p2, p3, p4], 1
    )

    # Cadeira
    chair_rect = pygame.Rect(
        x - 6, y + h + 2, 12, 10
    )

    pygame.draw.ellipse(
        surf, C_CHAIR_SHADE,
        chair_rect
    )

    pygame.draw.ellipse(
        surf, C_CHAIR_ORANGE,
        (x - 5, y + h + 2, 10, 8)
    )

    pygame.draw.ellipse(
        surf, C_CHAIR_LIGHT,
        (x - 3, y + h + 3, 6, 3)
    )

    pygame.draw.ellipse(
        surf, C_OUTLINE,
        chair_rect, 1
    )


# RENDERIZAÇÃO COMPLETA
def render_room():

    draw_room(canvas)

    draw_smartboard_and_projectors(
        canvas,
        center_x=160,
        top_y=16
    )

    draw_classroom_props(canvas)

    # 24 carteiras: 6 colunas x 4 fileiras
    cols = 6
    start_x = 56
    spacing_x = 41

    row_y_positions = [78, 108, 146, 176]

    for row_y in row_y_positions:
        for col in range(cols):

            desk_x = start_x + col * spacing_x

            draw_student_desk_and_orange_chair(
                canvas,
                desk_x,
                row_y
            )