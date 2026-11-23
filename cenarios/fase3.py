import pygame
import sys

# Inicialização
pygame.init()

# Resolução interna estilo GBA (pixel art) e janela escalada 3x
INTERNAL_W, INTERNAL_H = 320, 240
SCALE = 3
SCREEN_W, SCREEN_H = INTERNAL_W * SCALE, INTERNAL_H * SCALE

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Sala Moderna - Estilo Pokémon FireRed (Final)")
canvas = pygame.Surface((INTERNAL_W, INTERNAL_H))
clock = pygame.time.Clock()

# Paleta de Cores fiel à versão final
C_BG_VOID       = (40, 46, 56)       # Fundo externo escuro
C_WALL_TOP      = (140, 148, 136)    # Topo da parede
C_WALL_MAIN     = (168, 174, 152)    # Parede verde-acinzentada moderna (estilo GBA)
C_WALL_BASE     = (104, 112, 116)    # Rodapé escuro
C_OUTLINE       = (44, 48, 56)       # Contorno pixel art

C_FLOOR_WHITE_1 = (244, 246, 248)    # Piso branco principal
C_FLOOR_WHITE_2 = (232, 236, 240)    # Variação sutil das tábuas brancas
C_FLOOR_LINE    = (204, 210, 218)    # Linhas do piso branco
C_FLOOR_SHADOW  = (184, 190, 200)    # Sombra projetada no chão branco

C_DESK_TOP      = (248, 250, 252)    # Tampo branco da carteira
C_DESK_EDGE     = (140, 148, 160)    # Frente/estrutura da carteira
C_DESK_LEG      = (88, 96, 108)      # Pés da carteira

C_CHAIR_ORANGE  = (224, 136, 64)     # Assento laranja moderno
C_CHAIR_SHADE   = (184, 100, 40)     # Sombra do assento laranja
C_CHAIR_LIGHT   = (244, 168, 96)     # Brilho no assento laranja

C_PROF_WOOD_1   = (148, 96, 76)      # Tampo madeira mesa do professor
C_PROF_WOOD_2   = (112, 70, 56)      # Frente mesa do professor

C_PROJ_BODY     = (168, 176, 192)    # Corpo metálico do projetor
C_PROJ_SHADE    = (112, 120, 136)    # Sombra do projetor
C_PROJ_LENS     = (56, 64, 80)       # Lente do projetor


def draw_room(surf):
    surf.fill(C_BG_VOID)

    room_x, room_y = 24, 10
    room_w, room_h = 272, 220
    wall_h = 38
    floor_y = room_y + wall_h
    floor_h = room_h - wall_h

    # 1. Piso branco em réguas horizontais
    pygame.draw.rect(surf, C_FLOOR_WHITE_1, (room_x, floor_y, room_w, floor_h))

    plank_h = 10
    plank_w = 48
    for y in range(floor_y, floor_y + floor_h, plank_h):
        row = (y - floor_y) // plank_h
        offset = (plank_w // 2) if row % 2 == 1 else 0
        pygame.draw.line(surf, C_FLOOR_LINE, (room_x, y), (room_x + room_w - 1, y))
        for x in range(room_x + offset, room_x + room_w, plank_w):
            if (x // plank_w + row) % 2 == 0:
                w = min(plank_w, room_x + room_w - x)
                h = min(plank_h - 1, floor_y + floor_h - y - 1)
                if h > 0:
                    pygame.draw.rect(surf, C_FLOOR_WHITE_2, (x, y + 1, w, h))
            pygame.draw.line(surf, C_FLOOR_LINE, (x, y), (x, min(y + plank_h, floor_y + floor_h - 1)))

    # Sombra da parede no piso branco
    pygame.draw.rect(surf, C_FLOOR_SHADOW, (room_x, floor_y, room_w, 3))

    # 2. Paredes (estilo FireRed)
    pygame.draw.rect(surf, C_WALL_TOP, (room_x, room_y, room_w, 5))
    pygame.draw.rect(surf, C_WALL_MAIN, (room_x, room_y + 5, room_w, wall_h - 9))
    pygame.draw.rect(surf, C_WALL_BASE, (room_x, floor_y - 4, room_w, 4))

    # Moldura externa da sala
    pygame.draw.rect(surf, C_OUTLINE, (room_x - 1, room_y - 1, room_w + 2, room_h + 2), 1)
    pygame.draw.line(surf, C_OUTLINE, (room_x, floor_y), (room_x + room_w - 1, floor_y))

    # Porta na parede direita (conforme imagem)
    door_x = room_x + room_w - 2
    door_y = floor_y + 62
    pygame.draw.rect(surf, (156, 104, 64), (door_x, door_y, 5, 34))
    pygame.draw.rect(surf, C_OUTLINE, (door_x, door_y, 5, 34), 1)


def draw_smartboard_and_projectors(surf, center_x, top_y):
    """Lousa digital central + dois projetores laterais."""
    # --- Lousa Digital ---
    bw, bh = 86, 26
    bx = center_x - bw // 2
    by = top_y

    # Moldura externa
    pygame.draw.rect(surf, (136, 144, 164), (bx, by, bw, bh))
    pygame.draw.rect(surf, C_OUTLINE, (bx, by, bw, bh), 1)
    # Controles laterais da lousa
    pygame.draw.line(surf, C_OUTLINE, (bx + 7, by), (bx + 7, by + bh - 1))
    pygame.draw.line(surf, C_OUTLINE, (bx + bw - 8, by), (bx + bw - 8, by + bh - 1))
    # Tela azul clara com reflexo diagonal
    pygame.draw.rect(surf, (184, 216, 232), (bx + 9, by + 3, bw - 18, bh - 6))
    pygame.draw.rect(surf, C_OUTLINE, (bx + 9, by + 3, bw - 18, bh - 6), 1)
    pygame.draw.polygon(surf, (216, 236, 248), [
        (bx + 14, by + 4), (bx + 24, by + 4),
        (bx + 15, by + bh - 5), (bx + 10, by + bh - 5)
    ])
    # Suporte inferior da lousa
    pygame.draw.rect(surf, (136, 144, 164), (center_x - 16, by + bh, 32, 3))
    pygame.draw.rect(surf, C_OUTLINE, (center_x - 16, by + bh, 32, 3), 1)

    # --- Dois Projetores (um de cada lado do quadro) ---
    for px in [bx - 24, bx + bw + 8]:
        py = top_y - 2
        # Suporte superior de teto/parede
        pygame.draw.rect(surf, C_PROJ_BODY, (px + 2, py, 12, 5))
        pygame.draw.rect(surf, C_OUTLINE, (px + 2, py, 12, 5), 1)
        # Haste vertical
        pygame.draw.rect(surf, C_PROJ_SHADE, (px + 6, py + 5, 4, 8))
        pygame.draw.rect(surf, C_OUTLINE, (px + 6, py + 5, 4, 8), 1)
        # Corpo do projetor
        pygame.draw.rect(surf, C_PROJ_BODY, (px, py + 13, 16, 11))
        pygame.draw.rect(surf, C_PROJ_SHADE, (px, py + 20, 16, 4))
        pygame.draw.rect(surf, C_OUTLINE, (px, py + 13, 16, 11), 1)
        # Lente frontal
        pygame.draw.rect(surf, C_PROJ_LENS, (px + 2, py + 18, 5, 5))
        pygame.draw.rect(surf, (160, 200, 230), (px + 3, py + 19, 2, 2))


def draw_classroom_props(surf):
    """Mesa do professor, lixeira, alarme vermelho e planta."""
    # --- Cadeira e Mesa do Professor (canto superior esquerdo) ---
    px, py = 28, 52
    # Cadeira marrom atrás da mesa
    pygame.draw.rect(surf, C_PROF_WOOD_1, (px + 18, py - 12, 12, 12))
    pygame.draw.rect(surf, C_OUTLINE, (px + 18, py - 12, 12, 12), 1)

    # Sombra da mesa
    pygame.draw.rect(surf, C_FLOOR_SHADOW, (px + 1, py + 20, 48, 3))
    # Tampo e frente
    pygame.draw.rect(surf, C_PROF_WOOD_1, (px, py, 48, 14))
    pygame.draw.rect(surf, C_PROF_WOOD_2, (px, py + 14, 48, 6))
    pygame.draw.rect(surf, C_OUTLINE, (px, py, 48, 20), 1)
    pygame.draw.line(surf, C_OUTLINE, (px, py + 14), (px + 47, py + 14))

    # Notebook fechado/aberto sobre a mesa
    pygame.draw.rect(surf, (136, 148, 172), (px + 18, py + 3, 13, 8))
    pygame.draw.rect(surf, C_OUTLINE, (px + 18, py + 3, 13, 8), 1)

    # --- Lixeira metálica ao lado da mesa ---
    tx, ty = px + 51, py + 7
    pygame.draw.rect(surf, (168, 176, 188), (tx, ty, 9, 11))
    pygame.draw.rect(surf, (96, 104, 116), (tx + 2, ty + 1, 5, 3))
    pygame.draw.rect(surf, C_OUTLINE, (tx, ty, 9, 11), 1)

    # --- Painel/Alarme vermelho na parede direita ---
    ax, ay = 250, 22
    pygame.draw.rect(surf, (200, 68, 68), (ax, ay, 10, 11))
    pygame.draw.rect(surf, (240, 240, 240), (ax + 3, ay + 3, 4, 4))
    pygame.draw.rect(surf, C_OUTLINE, (ax, ay, 10, 11), 1)

    # --- Vaso de Planta no canto superior direito ---
    vx, vy = 266, 46
    pygame.draw.rect(surf, C_FLOOR_SHADOW, (vx + 1, vy + 18, 12, 3))
    # Vaso
    pygame.draw.rect(surf, (168, 152, 112), (vx + 2, vy + 10, 10, 8))
    pygame.draw.rect(surf, C_OUTLINE, (vx + 2, vy + 10, 10, 8), 1)
    # Folhagem verde
    pygame.draw.ellipse(surf, (88, 160, 96), (vx, vy, 14, 11))
    pygame.draw.ellipse(surf, C_OUTLINE, (vx, vy, 14, 11), 1)


def draw_student_desk_and_orange_chair(surf, x, y):
    """Carteira triangular/trapezoidal branca + cadeira redonda laranja."""
    top_w = 16
    bot_w = 24
    h = 12

    p1 = (x - top_w // 2, y)
    p2 = (x + top_w // 2, y)
    p3 = (x + bot_w // 2, y + h)
    p4 = (x - bot_w // 2, y + h)

    # Sombra no piso branco
    pygame.draw.rect(surf, C_FLOOR_SHADOW, (p4[0] + 1, p4[1] + 5, bot_w - 1, 5))

    # Pés da mesa
    pygame.draw.rect(surf, C_DESK_LEG, (p4[0] + 1, p4[1] + 2, 3, 6))
    pygame.draw.rect(surf, C_OUTLINE, (p4[0] + 1, p4[1] + 2, 3, 6), 1)
    pygame.draw.rect(surf, C_DESK_LEG, (p3[0] - 3, p3[1] + 2, 3, 6))
    pygame.draw.rect(surf, C_OUTLINE, (p3[0] - 3, p3[1] + 2, 3, 6), 1)

    # Frente da mesa (espessura 3D)
    pygame.draw.rect(surf, C_DESK_EDGE, (p4[0], p4[1], bot_w + 1, 3))
    pygame.draw.rect(surf, C_OUTLINE, (p4[0], p4[1], bot_w + 1, 3), 1)

    # Tampo triangular branco
    pygame.draw.polygon(surf, C_DESK_TOP, [p1, p2, p3, p4])
    pygame.draw.polygon(surf, C_OUTLINE, [p1, p2, p3, p4], 1)

    # Cadeira redonda laranja logo abaixo da mesa
    chair_rect = pygame.Rect(x - 6, y + h + 2, 12, 10)
    pygame.draw.ellipse(surf, C_CHAIR_SHADE, chair_rect)
    pygame.draw.ellipse(surf, C_CHAIR_ORANGE, (x - 5, y + h + 2, 10, 8))
    pygame.draw.ellipse(surf, C_CHAIR_LIGHT, (x - 3, y + h + 3, 6, 3))
    pygame.draw.ellipse(surf, C_OUTLINE, chair_rect, 1)


def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        # Desenha toda a cena em camadas
        draw_room(canvas)
        draw_smartboard_and_projectors(canvas, center_x=160, top_y=16)
        draw_classroom_props(canvas)

        # 24 carteiras triangulares (6 colunas x 4 fileiras com corredor central)
        cols = 6
        start_x = 56
        spacing_x = 41
        row_y_positions = [78, 108, 146, 176]

        for row_y in row_y_positions:
            for col in range(cols):
                desk_x = start_x + col * spacing_x
                draw_student_desk_and_orange_chair(canvas, desk_x, row_y)

        # Escala sem perda de nitidez (pixel art)
        scaled_surface = pygame.transform.scale(canvas, (SCREEN_W, SCREEN_H))
        screen.blit(scaled_surface, (0, 0))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()