import pygame
from constantes import (TILE, SCALE, COLS, ROWS, WIDTH, HEIGHT, PALETTE_FASE1)

canvas = pygame.Surface((WIDTH, HEIGHT))

def draw_floor():
    # Desenha o piso quadriculado.
    for r in range(2, ROWS):
        for c in range(COLS):
            color = (
                PALETTE_FASE1['floor_light']
                if (r + c) % 2 == 0
                else PALETTE_FASE1['floor_dark']
            )
            pygame.draw.rect(
                canvas, color,
                (c * TILE, r * TILE, TILE, TILE)
            )
            pygame.draw.rect(
                canvas, PALETTE_FASE1['floor_grid'],
                (c * TILE, r * TILE, TILE, TILE), 1
            )

def draw_glass_board(x, y, w, h):
    # Desenha um quadro de vidro.
    pygame.draw.rect(
        canvas, PALETTE_FASE1['glass_frame'],
        (x, y, w, h)
    )
    pygame.draw.rect(
        canvas, PALETTE_FASE1['glass_bg'],
        (x + 2, y + 2, w - 4, h - 4)
    )
    for i in range(h - 6):
        pygame.draw.line(
            canvas, PALETTE_FASE1['glass_glare'],
            (x + 6 + i, y + h - 4 - i),
            (x + 11 + i, y + h - 4 - i)
        )
        pygame.draw.line(
            canvas, PALETTE_FASE1['glass_glare'],
            (x + 24 + i, y + h - 4 - i),
            (x + 27 + i, y + h - 4 - i)
        )
    pygame.draw.rect(
        canvas, PALETTE_FASE1['pc_shade'],
        (x + 1, y + h - 2, w - 2, 2)
    )
    pygame.draw.rect(
        canvas, (200, 64, 64),
        (x + 14, y + h - 3, 4, 2)
    )
    pygame.draw.rect(
        canvas, (64, 104, 184),
        (x + 20, y + h - 3, 4, 2)
    )
    pygame.draw.rect(
        canvas, (120, 112, 104),
        (x + 32, y + h - 4, 8, 3)
    )
    pygame.draw.rect(
        canvas, PALETTE_FASE1['black'],
        (x, y, w, h), 1
    )

def draw_walls_and_front():
    # Desenha paredes, quadros, TV e porta.
    pygame.draw.rect(
        canvas, PALETTE_FASE1['wall_top'],
        (0, 0, COLS * TILE, 8)
    )
    pygame.draw.rect(
        canvas, PALETTE_FASE1['wall_front'],
        (0, 8, COLS * TILE, 26)
    )
    pygame.draw.line(
        canvas, PALETTE_FASE1['black'],
        (0, 33), (COLS * TILE, 33), 1
    )
    draw_glass_board(24, 10, 56, 20)

    # TV central
    pygame.draw.rect(
        canvas, PALETTE_FASE1['tv_frame'],
        (108, 9, 64, 24)
    )
    pygame.draw.rect(
        canvas, PALETTE_FASE1['tv_screen'],
        (111, 12, 58, 18)
    )
    pygame.draw.rect(
        canvas, PALETTE_FASE1['tv_frame'],
        (126, 33, 28, 3)
    )
    pygame.draw.rect(
        canvas, PALETTE_FASE1['black'],
        (126, 33, 28, 3), 1
    )
    pygame.draw.rect(
        canvas, PALETTE_FASE1['black'],
        (108, 9, 64, 24), 1
    )
    draw_glass_board(198, 10, 56, 20)
    # Bordas laterais
    pygame.draw.rect(
        canvas, PALETTE_FASE1['wall_trim'],
        (0, 0, 8, ROWS * TILE)
    )
    pygame.draw.rect(
        canvas, PALETTE_FASE1['wall_trim'],
        (COLS * TILE - 8, 0, 8, ROWS * TILE)
    )
    pygame.draw.rect(
        canvas, PALETTE_FASE1['black'],
        (0, 0, COLS * TILE, ROWS * TILE), 1
    )
    # Porta lateral
    pygame.draw.rect(
        canvas, PALETTE_FASE1['door_wood'],
        (8, 146, 5, 36)
    )
    pygame.draw.rect(
        canvas, PALETTE_FASE1['door_dark'],
        (11, 146, 2, 36)
    )
    pygame.draw.rect(
        canvas, PALETTE_FASE1['black'],
        (8, 146, 5, 36), 1
    )
    pygame.draw.rect(
        canvas, PALETTE_FASE1['pc_body'],
        (12, 163, 2, 2)
    )

def draw_totem_back(x, y):
    # Desenha o totem visto de costas.
    pygame.draw.rect(
        canvas, PALETTE_FASE1['desk_shadow'],
        (x + 1, y + 32, 22, 3)
    )
    pygame.draw.rect(
        canvas, PALETTE_FASE1['totem_body'],
        (x, y + 4, 24, 28)
    )
    pygame.draw.rect(
        canvas, PALETTE_FASE1['totem_top'],
        (x + 2, y, 20, 6)
    )
    pygame.draw.line(
        canvas, PALETTE_FASE1['totem_shade'],
        (x + 1, y + 6), (x + 1, y + 30), 2
    )
    pygame.draw.line(
        canvas, PALETTE_FASE1['totem_shade'],
        (x + 22, y + 6), (x + 22, y + 30), 2
    )
    pygame.draw.line(
        canvas, PALETTE_FASE1['totem_shade'],
        (x + 1, y + 30), (x + 22, y + 30), 2
    )
    pygame.draw.rect(
        canvas, PALETTE_FASE1['black'],
        (x, y + 2, 24, 30), 1
    )
    pygame.draw.line(
        canvas, PALETTE_FASE1['black'],
        (x + 2, y), (x + 21, y), 1
    )

def draw_workstation(x, y):
    # Desenha computador, teclado, mouse e cadeira.
    # Monitor
    pygame.draw.rect(
        canvas, PALETTE_FASE1['pc_body'],
        (x + 3, y - 5, 14, 11)
    )
    pygame.draw.rect(
        canvas, PALETTE_FASE1['pc_shade'],
        (x + 4, y + 4, 12, 2)
    )
    pygame.draw.rect(
        canvas, PALETTE_FASE1['screen_dark'],
        (x + 5, y - 3, 10, 6)
    )
    pygame.draw.line(
        canvas, PALETTE_FASE1['screen_glare'],
        (x + 6, y - 2), (x + 10, y - 2), 1
    )
    pygame.draw.rect(
        canvas, PALETTE_FASE1['black'],
        (x + 3, y - 5, 14, 11), 1
    )

    # Teclado
    pygame.draw.rect(
        canvas, PALETTE_FASE1['pc_body'],
        (x + 2, y + 8, 16, 5)
    )
    pygame.draw.line(
        canvas, PALETTE_FASE1['pc_shade'],
        (x + 4, y + 10), (x + 15, y + 10), 1
    )
    pygame.draw.rect(
        canvas, PALETTE_FASE1['black'],
        (x + 2, y + 8, 16, 5), 1
    )
    # Mouse
    pygame.draw.rect(
        canvas, PALETTE_FASE1['pc_body'],
        (x + 20, y + 9, 3, 4)
    )
    pygame.draw.rect(
        canvas, PALETTE_FASE1['black'],
        (x + 20, y + 9, 3, 4), 1
    )

    # Cadeira
    cx, cy = x + 5, y + 19
    pygame.draw.rect(
        canvas, PALETTE_FASE1['desk_shadow'],
        (cx + 1, cy + 8, 8, 2)
    )
    pygame.draw.line(
        canvas, PALETTE_FASE1['black'],
        (cx + 2, cy + 7), (cx + 2, cy + 9), 1
    )
    pygame.draw.line(
        canvas, PALETTE_FASE1['black'],
        (cx + 7, cy + 7), (cx + 7, cy + 9), 1
    )
    pygame.draw.rect(
        canvas, PALETTE_FASE1['chair_red'],
        (cx, cy, 10, 7)
    )
    pygame.draw.rect(
        canvas, PALETTE_FASE1['chair_dark'],
        (cx + 1, cy + 5, 8, 2)
    )
    pygame.draw.rect(
        canvas, PALETTE_FASE1['black'],
        (cx, cy, 10, 7), 1
    )

def draw_desk_row(x, y, num_pcs, spacing=30, total_width=None):
    # Desenha uma bancada com computadores.
    width = total_width if total_width else (
        num_pcs * spacing + 4
    )
    height = 15
    # Pernas
    pygame.draw.rect(
        canvas, PALETTE_FASE1['desk_leg'],
        (x + 1, y + height, 4, 4)
    )
    pygame.draw.rect(
        canvas, PALETTE_FASE1['black'],
        (x + 1, y + height, 4, 4), 1
    )
    pygame.draw.rect(
        canvas, PALETTE_FASE1['desk_leg'],
        (x + width - 5, y + height, 4, 4)
    )
    pygame.draw.rect(
        canvas, PALETTE_FASE1['black'],
        (x + width - 5, y + height, 4, 4), 1
    )

    # Tampo
    pygame.draw.rect(
        canvas, PALETTE_FASE1['desk_top'],
        (x, y, width, height - 3)
    )
    pygame.draw.rect(
        canvas, PALETTE_FASE1['desk_edge'],
        (x, y + height - 3, width, 3)
    )
    pygame.draw.rect(
        canvas, PALETTE_FASE1['black'],
        (x, y, width, height), 1
    )
    # Computadores
    for i in range(num_pcs):
        draw_workstation(
            x + 4 + i * spacing,
            y + 1
        )

def render_room():
    """Renderiza toda a sala."""
    draw_floor()
    draw_walls_and_front()
    draw_totem_back(246, 36)

    # Lado esquerdo
    draw_desk_row(
        10, 56, num_pcs=3,
        spacing=28, total_width=86
    )
    draw_desk_row(
        10, 90, num_pcs=3,
        spacing=28, total_width=86
    )
    draw_desk_row(
        10, 202, num_pcs=2,
        spacing=34, total_width=70
    )
    draw_desk_row(
        10, 238, num_pcs=2,
        spacing=34, total_width=70
    )
    # Lado direito
    right_y_positions = [84, 122, 160, 198, 236]
    for ry in right_y_positions:
        draw_desk_row(
            168, ry, num_pcs=3,
            spacing=31, total_width=108
        )