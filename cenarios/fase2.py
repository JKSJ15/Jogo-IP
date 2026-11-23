import sys
import pygame

# --- Configurações de Tela (Proporção 4:3 estilo GBA escalada 3x) ---
NATIVE_W, NATIVE_H = 320, 240
SCALE = 3
WINDOW_W, WINDOW_H = NATIVE_W * SCALE, NATIVE_H * SCALE
FPS = 60

# --- Paleta Pokémon FireRed (Branco, Cinza Moderno & Azul) ---
C_BG_FRAME = (248, 249, 251)
C_OUTLINE = (32, 36, 44)
C_WHITE = (252, 253, 255)
C_WALL_LIGHT = (232, 235, 240)
C_WALL_MID = (206, 211, 219)
C_WALL_DARK = (156, 163, 174)
C_BASEBOARD = (102, 109, 120)

C_FLOOR_TILE = (241, 244, 248)
C_FLOOR_GRID = (205, 211, 220)
C_SHADOW = (182, 190, 202)

# Vidro da porta
C_GLASS_BG = (212, 229, 242)
C_GLASS_SHADE = (184, 206, 224)
C_GLASS_SHINE = (245, 251, 255)
C_METAL = (130, 140, 152)

# Azul das almofadas e cadeira do professor
C_BLUE_LIGHT = (122, 182, 248)
C_BLUE_MID = (64, 134, 222)
C_BLUE_DARK = (36, 84, 158)
C_BLUE_DEEP = (24, 56, 112)


def draw_room_architecture(surf):
    """Desenha piso quadriculado, paredes em perspectiva GBA e interfone."""
    surf.fill(C_BG_FRAME)

    # Paredes e piso interno
    room_rect = pygame.Rect(12, 10, 296, 222)
    pygame.draw.rect(surf, C_WALL_LIGHT, room_rect)

    # Parede superior (y: 10..64)
    pygame.draw.rect(surf, C_WALL_MID, (12, 10, 296, 6))
    pygame.draw.line(surf, C_WALL_DARK, (20, 16), (300, 16))
    pygame.draw.rect(surf, C_WALL_LIGHT, (20, 17, 280, 43))
    # Rodapé escuro
    pygame.draw.rect(surf, C_BASEBOARD, (20, 60, 280, 4))
    pygame.draw.line(surf, C_OUTLINE, (20, 64), (300, 64))

    # Paredes laterais (esquerda e direita)
    pygame.draw.rect(surf, C_WALL_MID, (12, 10, 8, 222))
    pygame.draw.rect(surf, C_WALL_MID, (300, 10, 8, 222))
    pygame.draw.line(surf, C_WALL_DARK, (20, 16), (20, 232))
    pygame.draw.line(surf, C_WALL_DARK, (300, 16), (300, 232))
    pygame.draw.line(surf, C_WALL_DARK, (12, 10), (20, 16))
    pygame.draw.line(surf, C_WALL_DARK, (308, 10), (300, 16))

    # Piso quadriculado 16x16 (y: 65..232)
    floor_rect = pygame.Rect(21, 65, 279, 167)
    pygame.draw.rect(surf, C_FLOOR_TILE, floor_rect)
    for gx in range(21, 300, 16):
        pygame.draw.line(surf, C_FLOOR_GRID, (gx, 65), (gx, 231))
    for gy in range(65, 232, 16):
        pygame.draw.line(surf, C_FLOOR_GRID, (21, gy), (299, gy))

    # Interfone / controle na parede lateral esquerda
    pygame.draw.rect(surf, C_OUTLINE, (15, 31, 9, 20))
    pygame.draw.rect(surf, C_WHITE, (16, 32, 5, 18))
    pygame.draw.rect(surf, C_WALL_DARK, (21, 32, 2, 18))
    pygame.draw.rect(surf, C_BASEBOARD, (17, 36, 3, 5))


def draw_full_glass_door(surf, x=34, y=24):
    """Porta moderna toda de vidro com ferragens metálicas minimalistas."""
    w, h = 32, 40
    # Sombra interna na parede
    pygame.draw.rect(surf, C_WALL_DARK, (x - 1, y - 1, w + 2, h + 1))
    # Folha inteiriça de vidro temperado
    pygame.draw.rect(surf, C_OUTLINE, (x, y, w, h), 1)
    pygame.draw.rect(surf, C_GLASS_BG, (x + 1, y + 1, w - 2, h - 2))

    # Reflexos diagonais no vidro
    pygame.draw.polygon(
        surf,
        C_GLASS_SHINE,
        [(x + 4, y + 3), (x + 12, y + 3), (x + 3, y + 16), (x + 3, y + 9)],
    )
    pygame.draw.polygon(
        surf,
        C_GLASS_SHINE,
        [(x + 16, y + 3), (x + 20, y + 3), (x + 3, y + 27), (x + 3, y + 22)],
    )
    # Faixa sutil de profundidade na base do vidro
    pygame.draw.rect(surf, C_GLASS_SHADE, (x + 1, y + h - 5, w - 2, 4))

    # Dobradiças minimalistas à esquerda e puxador vertical metálico à direita
    pygame.draw.rect(surf, C_OUTLINE, (x, y + 5, 3, 4))
    pygame.draw.rect(surf, C_METAL, (x + 1, y + 6, 2, 2))
    pygame.draw.rect(surf, C_OUTLINE, (x, y + h - 9, 3, 4))
    pygame.draw.rect(surf, C_METAL, (x + 1, y + h - 8, 2, 2))

    pygame.draw.rect(surf, C_OUTLINE, (x + w - 6, y + 15, 3, 12))
    pygame.draw.rect(surf, C_WHITE, (x + w - 5, y + 16, 1, 10))


def draw_whiteboard(surf, x=110, y=15):
    """Lousa branca interativa na parede superior central."""
    w, h = 100, 44
    pygame.draw.rect(surf, C_OUTLINE, (x, y, w, h))
    pygame.draw.rect(surf, C_WALL_DARK, (x + 1, y + 1, w - 2, h - 2))
    pygame.draw.rect(surf, C_WHITE, (x + 3, y + 3, w - 6, h - 8))

    # Esquemas/gráficos sutis desenhados na lousa
    pygame.draw.rect(surf, C_WALL_MID, (x + 31, y + 16, 14, 12), 1)
    pygame.draw.lines(
        surf, C_WALL_MID, False, [(x + 34, y + 24), (x + 37, y + 20), (x + 40, y + 23), (x + 42, y + 19)], 1
    )
    pygame.draw.lines(
        surf,
        C_WALL_MID,
        False,
        [(x + 76, y + 17), (x + 76, y + 27), (x + 89, y + 27)],
        1,
    )
    pygame.draw.lines(
        surf,
        C_WALL_MID,
        False,
        [(x + 77, y + 25), (x + 80, y + 21), (x + 83, y + 24), (x + 87, y + 19)],
        1,
    )

    # Bandeja inferior com apagador e pincéis
    pygame.draw.rect(surf, C_BASEBOARD, (x + 1, y + h - 4, w - 2, 3))
    pygame.draw.rect(surf, C_OUTLINE, (x + 58, y + h - 6, 10, 3))
    pygame.draw.rect(surf, C_BLUE_MID, (x + 42, y + h - 5, 4, 2))
    pygame.draw.rect(surf, (214, 110, 110), (x + 36, y + h - 5, 4, 2))


def draw_teacher_station(surf):
    """Mesa branca inclinada do professor e cadeira giratória azul (canto superior direito)."""
    # --- Mesa do professor (perspectiva 2.5D) ---
    desk_top = [(228, 52), (252, 52), (264, 74), (240, 74)]
    desk_front = [(240, 74), (264, 74), (264, 92), (240, 92)]
    desk_side = [(228, 52), (240, 74), (240, 92), (228, 69)]

    pygame.draw.polygon(surf, C_SHADOW, [(230, 89), (266, 89), (266, 94), (230, 94)])
    pygame.draw.polygon(surf, C_WALL_MID, desk_side)
    pygame.draw.polygon(surf, C_OUTLINE, desk_side, 1)
    pygame.draw.polygon(surf, C_WALL_DARK, desk_front)
    pygame.draw.polygon(surf, C_OUTLINE, desk_front, 1)
    pygame.draw.polygon(surf, C_WHITE, desk_top)
    pygame.draw.polygon(surf, C_OUTLINE, desk_top, 1)

    # --- Cadeira giratória azul do professor ---
    cx, cy = 268, 42
    # Base giratória com rodízios
    pygame.draw.line(surf, C_OUTLINE, (cx + 12, cy + 25), (cx + 5, cy + 32), 2)
    pygame.draw.line(surf, C_OUTLINE, (cx + 12, cy + 25), (cx + 19, cy + 32), 2)
    pygame.draw.line(surf, C_OUTLINE, (cx + 12, cy + 25), (cx + 12, cy + 33), 2)
    pygame.draw.rect(surf, C_METAL, (cx + 10, cy + 25, 4, 4))

    # Assento estofado azul
    pygame.draw.rect(surf, C_OUTLINE, (cx + 3, cy + 16, 18, 9), border_radius=3)
    pygame.draw.rect(surf, C_BLUE_MID, (cx + 4, cy + 17, 16, 6), border_radius=2)
    pygame.draw.rect(surf, C_BLUE_LIGHT, (cx + 6, cy + 17, 12, 2))

    # Encosto ergonômico azul
    pygame.draw.rect(surf, C_OUTLINE, (cx + 7, cy + 1, 14, 16), border_radius=3)
    pygame.draw.rect(surf, C_BLUE_MID, (cx + 8, cy + 2, 12, 13), border_radius=2)
    pygame.draw.rect(surf, C_BLUE_LIGHT, (cx + 9, cy + 3, 9, 4))

    # Apoios de braço
    pygame.draw.rect(surf, C_OUTLINE, (cx + 1, cy + 12, 6, 4))
    pygame.draw.rect(surf, C_BLUE_DARK, (cx + 2, cy + 13, 4, 2))
    pygame.draw.rect(surf, C_OUTLINE, (cx + 18, cy + 13, 6, 4))
    pygame.draw.rect(surf, C_BLUE_DARK, (cx + 19, cy + 14, 4, 2))


def draw_center_table(surf, x=112, y=96):
    """Mesa retangular central da 1ª fileira."""
    w, h = 64, 26
    pygame.draw.rect(surf, C_SHADOW, (x + 2, y + h - 2, w - 4, 4))
    # Pernas frontais
    pygame.draw.rect(surf, C_OUTLINE, (x + 2, y + 18, 4, 9))
    pygame.draw.rect(surf, C_WALL_DARK, (x + 3, y + 19, 2, 7))
    pygame.draw.rect(surf, C_OUTLINE, (x + w - 6, y + 18, 4, 9))
    pygame.draw.rect(surf, C_WALL_DARK, (x + w - 5, y + 19, 2, 7))
    # Tampo branco e frente cinza
    pygame.draw.rect(surf, C_OUTLINE, (x, y, w, 20))
    pygame.draw.rect(surf, C_WHITE, (x + 1, y + 1, w - 2, 14))
    pygame.draw.rect(surf, C_WALL_MID, (x + 1, y + 15, w - 2, 4))


def draw_student_chair(surf, x, y):
    """
    Cadeira universitária estilo FireRed com almofada azul, encosto curvo inferior
    e prancheta branca acoplada no canto superior direito.
    """
    # Sombra no chão e pé central
    pygame.draw.ellipse(surf, C_SHADOW, (x + 2, y + 23, 20, 6))
    pygame.draw.rect(surf, C_OUTLINE, (x + 10, y + 25, 4, 4))

    # Prancheta branca superior direita + haste lateral
    pygame.draw.rect(surf, C_OUTLINE, (x + 11, y, 13, 12), border_radius=2)
    pygame.draw.rect(surf, C_WHITE, (x + 12, y + 1, 11, 8))
    pygame.draw.rect(surf, C_WALL_MID, (x + 12, y + 9, 11, 2))
    pygame.draw.rect(surf, C_OUTLINE, (x + 20, y + 11, 4, 11))
    pygame.draw.rect(surf, C_WALL_MID, (x + 21, y + 11, 2, 10))

    # Apoio de braço esquerdo curto
    pygame.draw.rect(surf, C_OUTLINE, (x, y + 11, 4, 9), border_radius=1)
    pygame.draw.rect(surf, C_BLUE_DARK, (x + 1, y + 12, 2, 6))

    # Almofada arredondada azul do assento
    pygame.draw.rect(surf, C_OUTLINE, (x + 2, y + 9, 19, 13), border_radius=5)
    pygame.draw.rect(surf, C_BLUE_MID, (x + 3, y + 10, 17, 10), border_radius=4)
    pygame.draw.ellipse(surf, C_BLUE_LIGHT, (x + 5, y + 11, 13, 5))

    # Encosto curvo azul-escuro envolvendo a base
    pygame.draw.rect(surf, C_OUTLINE, (x + 1, y + 17, 21, 9), border_radius=4)
    pygame.draw.rect(surf, C_BLUE_DARK, (x + 2, y + 18, 19, 6), border_radius=3)
    pygame.draw.line(surf, C_BLUE_DEEP, (x + 3, y + 23), (x + 19, y + 23))


def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_W, WINDOW_H))
    pygame.display.set_caption("Sala Moderna (Almofadas Azuis & Porta de Vidro) - Pokémon FireRed")
    native = pygame.Surface((NATIVE_W, NATIVE_H))
    clock = pygame.time.Clock()

    # Coordenadas exatas das 8 colunas e 4 fileiras de assentos
    cols_x = [32, 66, 100, 134, 168, 202, 236, 270]
    rows_y = [92, 128, 162, 196]

    chairs = []
    # Fileira 1: 1 cadeira à esquerda, mesa central, 3 cadeiras à direita
    chairs.append((cols_x[0], rows_y[0]))
    for c in (5, 6, 7):
        chairs.append((cols_x[c], rows_y[0]))

    # Fileiras 2, 3 e 4: 8 cadeiras distribuídas horizontalmente
    for r in (1, 2, 3):
        for cx in cols_x:
            chairs.append((cx, rows_y[r]))

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        # Renderização da cena
        draw_room_architecture(native)
        draw_full_glass_door(native, x=34, y=24)
        draw_whiteboard(native, x=110, y=15)
        draw_teacher_station(native)
        draw_center_table(native, x=112, y=96)

        for cx, cy in chairs:
            draw_student_chair(native, cx, cy)

        # Escala 3x preservando a nitidez pixel-art
        scaled = pygame.transform.scale(native, (WINDOW_W, WINDOW_H))
        screen.blit(scaled, (0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    main()