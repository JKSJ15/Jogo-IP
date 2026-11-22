import pygame
import sys

# Inicialização
pygame.init() 
TILE = 16
SCALE = 3  # Ampliação 3x para manter o visual nítido de Game Boy Color
COLS = 18
ROWS = 18
WIDTH = COLS * TILE * SCALE
HEIGHT = ROWS * TILE * SCALE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sala de Informática - Estilo Pokémon TCG (GBC)")
canvas = pygame.Surface((COLS * TILE, ROWS * TILE))

# Paleta de Cores Estilo Pokémon TCG (Game Boy Color)
PALETTE = {
    'black': (24, 24, 32),
    'white': (248, 248, 248),
    'floor_light': (224, 214, 184),
    'floor_dark': (184, 174, 144),
    'floor_grid': (168, 158, 130),
    'wall_top': (168, 184, 200),
    'wall_front': (104, 124, 142),
    'wall_trim': (44, 50, 56),
    'desk_top': (176, 128, 80),
    'desk_edge': (136, 92, 52),
    'desk_leg': (104, 68, 36),
    'desk_shadow': (144, 136, 112),
    'pc_body': (216, 214, 200),
    'pc_shade': (152, 150, 138),
    'screen_dark': (64, 72, 80),
    'screen_glare': (136, 152, 168),
    'chair_red': (176, 56, 56),
    'chair_dark': (120, 32, 32),
    'glass_bg': (192, 224, 224),
    'glass_glare': (236, 248, 248),
    'glass_frame': (136, 144, 152),
    'tv_frame': (68, 76, 84),
    'tv_screen': (44, 50, 58),
    'totem_body': (208, 200, 176),
    'totem_top': (228, 222, 200),
    'totem_shade': (160, 152, 132),
    'door_wood': (144, 96, 52),
    'door_dark': (96, 60, 28),
}

def draw_floor():
    """Desenha o piso quadriculado 100% homogêneo em toda a sala."""
    for r in range(2, ROWS):
        for c in range(COLS):
            color = PALETTE['floor_light'] if (r + c) % 2 == 0 else PALETTE['floor_dark']
            pygame.draw.rect(canvas, color, (c * TILE, r * TILE, TILE, TILE))
            pygame.draw.rect(canvas, PALETTE['floor_grid'], (c * TILE, r * TILE, TILE, TILE), 1)

def draw_glass_board(x, y, w, h):
    """Desenha um quadro de vidro com moldura metálica, reflexo diagonal e apagador."""
    # Moldura externa
    pygame.draw.rect(canvas, PALETTE['glass_frame'], (x, y, w, h))
    # Vidro
    pygame.draw.rect(canvas, PALETTE['glass_bg'], (x + 2, y + 2, w - 4, h - 4))
    # Reflexos diagonais característicos
    for i in range(h - 6):
        pygame.draw.line(canvas, PALETTE['glass_glare'], (x + 6 + i, y + h - 4 - i), (x + 11 + i, y + h - 4 - i))
        pygame.draw.line(canvas, PALETTE['glass_glare'], (x + 24 + i, y + h - 4 - i), (x + 27 + i, y + h - 4 - i))
    # Suporte inferior com apagador e marcadores
    pygame.draw.rect(canvas, PALETTE['pc_shade'], (x + 1, y + h - 2, w - 2, 2))
    pygame.draw.rect(canvas, (200, 64, 64), (x + 14, y + h - 3, 4, 2))   # Marcador vermelho
    pygame.draw.rect(canvas, (64, 104, 184), (x + 20, y + h - 3, 4, 2))  # Marcador azul
    pygame.draw.rect(canvas, (120, 112, 104), (x + 32, y + h - 4, 8, 3)) # Apagador
    pygame.draw.rect(canvas, PALETTE['black'], (x, y, w, h), 1)

def draw_walls_and_front():
    """Desenha a parede superior com os quadros de vidro, TV, bordas e porta lateral."""
    # Parede superior
    pygame.draw.rect(canvas, PALETTE['wall_top'], (0, 0, COLS * TILE, 8))
    pygame.draw.rect(canvas, PALETTE['wall_front'], (0, 8, COLS * TILE, 26))
    pygame.draw.line(canvas, PALETTE['black'], (0, 33), (COLS * TILE, 33), 1)

    # Quadro de vidro esquerdo
    draw_glass_board(24, 10, 56, 20)

    # TV central
    pygame.draw.rect(canvas, PALETTE['tv_frame'], (108, 9, 64, 24))
    pygame.draw.rect(canvas, PALETTE['tv_screen'], (111, 12, 58, 18))
    # Base da TV
    pygame.draw.rect(canvas, PALETTE['tv_frame'], (126, 33, 28, 3))
    pygame.draw.rect(canvas, PALETTE['black'], (126, 33, 28, 3), 1)
    pygame.draw.rect(canvas, PALETTE['black'], (108, 9, 64, 24), 1)

    # Quadro de vidro direito
    draw_glass_board(198, 10, 56, 20)

    # Bordas laterais escuras
    pygame.draw.rect(canvas, PALETTE['wall_trim'], (0, 0, 8, ROWS * TILE))
    pygame.draw.rect(canvas, PALETTE['wall_trim'], (COLS * TILE - 8, 0, 8, ROWS * TILE))
    pygame.draw.rect(canvas, PALETTE['black'], (0, 0, COLS * TILE, ROWS * TILE), 1)

    # Porta paralela à parede esquerda (entre o bloco superior e inferior de mesas)
    pygame.draw.rect(canvas, PALETTE['door_wood'], (8, 146, 5, 36))
    pygame.draw.rect(canvas, PALETTE['door_dark'], (11, 146, 2, 36))
    pygame.draw.rect(canvas, PALETTE['black'], (8, 146, 5, 36), 1)
    # Maçaneta
    pygame.draw.rect(canvas, PALETTE['pc_body'], (12, 163, 2, 2))

def draw_totem_back(x, y):
    """Desenha o totem/gabinete visto de costas (virado para o quadro)."""
    # Sombra no piso
    pygame.draw.rect(canvas, PALETTE['desk_shadow'], (x + 1, y + 32, 22, 3))
    # Corpo traseiro liso
    pygame.draw.rect(canvas, PALETTE['totem_body'], (x, y + 4, 24, 28))
    # Topo arredondado/chanfrado voltado para o quadro
    pygame.draw.rect(canvas, PALETTE['totem_top'], (x + 2, y, 20, 6))
    # Sombreamento lateral e inferior
    pygame.draw.line(canvas, PALETTE['totem_shade'], (x + 1, y + 6), (x + 1, y + 30), 2)
    pygame.draw.line(canvas, PALETTE['totem_shade'], (x + 22, y + 6), (x + 22, y + 30), 2)
    pygame.draw.line(canvas, PALETTE['totem_shade'], (x + 1, y + 30), (x + 22, y + 30), 2)
    # Contorno pixel art
    pygame.draw.rect(canvas, PALETTE['black'], (x, y + 2, 24, 30), 1)
    pygame.draw.line(canvas, PALETTE['black'], (x + 2, y), (x + 21, y), 1)

def draw_workstation(x, y):
    """Desenha monitor CRT, teclado, mouse e cadeira vermelha."""
    # Monitor CRT
    pygame.draw.rect(canvas, PALETTE['pc_body'], (x + 3, y - 5, 14, 11))
    pygame.draw.rect(canvas, PALETTE['pc_shade'], (x + 4, y + 4, 12, 2))
    pygame.draw.rect(canvas, PALETTE['screen_dark'], (x + 5, y - 3, 10, 6))
    pygame.draw.line(canvas, PALETTE['screen_glare'], (x + 6, y - 2), (x + 10, y - 2), 1)
    pygame.draw.rect(canvas, PALETTE['black'], (x + 3, y - 5, 14, 11), 1)

    # Teclado
    pygame.draw.rect(canvas, PALETTE['pc_body'], (x + 2, y + 8, 16, 5))
    pygame.draw.line(canvas, PALETTE['pc_shade'], (x + 4, y + 10), (x + 15, y + 10), 1)
    pygame.draw.rect(canvas, PALETTE['black'], (x + 2, y + 8, 16, 5), 1)

    # Mouse
    pygame.draw.rect(canvas, PALETTE['pc_body'], (x + 20, y + 9, 3, 4))
    pygame.draw.rect(canvas, PALETTE['black'], (x + 20, y + 9, 3, 4), 1)

    # Cadeira vermelha giratória abaixo da mesa
    cx, cy = x + 5, y + 19
    pygame.draw.rect(canvas, PALETTE['desk_shadow'], (cx + 1, cy + 8, 8, 2))
    # Base/rodinhas
    pygame.draw.line(canvas, PALETTE['black'], (cx + 2, cy + 7), (cx + 2, cy + 9), 1)
    pygame.draw.line(canvas, PALETTE['black'], (cx + 7, cy + 7), (cx + 7, cy + 9), 1)
    # Assento e encosto
    pygame.draw.rect(canvas, PALETTE['chair_red'], (cx, cy, 10, 7))
    pygame.draw.rect(canvas, PALETTE['chair_dark'], (cx + 1, cy + 5, 8, 2))
    pygame.draw.rect(canvas, PALETTE['black'], (cx, cy, 10, 7), 1)

def draw_desk_row(x, y, num_pcs, spacing=30, total_width=None):
    """Desenha uma bancada contínua com N computadores."""
    width = total_width if total_width else (num_pcs * spacing + 4)
    height = 15

    # Pernas da mesa
    pygame.draw.rect(canvas, PALETTE['desk_leg'], (x + 1, y + height, 4, 4))
    pygame.draw.rect(canvas, PALETTE['black'], (x + 1, y + height, 4, 4), 1)
    pygame.draw.rect(canvas, PALETTE['desk_leg'], (x + width - 5, y + height, 4, 4))
    pygame.draw.rect(canvas, PALETTE['black'], (x + width - 5, y + height, 4, 4), 1)

    # Tampo e borda frontal
    pygame.draw.rect(canvas, PALETTE['desk_top'], (x, y, width, height - 3))
    pygame.draw.rect(canvas, PALETTE['desk_edge'], (x, y + height - 3, width, 3))
    pygame.draw.rect(canvas, PALETTE['black'], (x, y, width, height), 1)

    # Computadores
    for i in range(num_pcs):
        draw_workstation(x + 4 + i * spacing, y + 1)

def render_room():
    draw_floor()
    draw_walls_and_front()

    # Totem virado para o quadro (canto superior direito)
    draw_totem_back(246, 36)

    # --- LADO ESQUERDO (2 bancadas de 3 PCs no topo + porta + 2 bancadas de 2 PCs embaixo) ---
    draw_desk_row(10, 56, num_pcs=3, spacing=28, total_width=86)
    draw_desk_row(10, 90, num_pcs=3, spacing=28, total_width=86)

    # Espaço livre para a porta paralela à parede (y ~ 146 a 182)

    draw_desk_row(10, 202, num_pcs=2, spacing=34, total_width=70)
    draw_desk_row(10, 238, num_pcs=2, spacing=34, total_width=70)

    # --- LADO DIREITO (5 bancadas contínuas, cada uma com 3 PCs e 3 cadeiras) ---
    right_y_positions = [84, 122, 160, 198, 236]
    for ry in right_y_positions:
        draw_desk_row(168, ry, num_pcs=3, spacing=31, total_width=108)

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            # Pressione 'S' para exportar a imagem em PNG
            pygame.image.save(screen, "sala_pokemon_tcg_final.png")
            print("Imagem salva como sala_pokemon_tcg_final.png!")

    render_room()
    scaled_surface = pygame.transform.scale(canvas, (WIDTH, HEIGHT))
    screen.blit(scaled_surface, (0, 0))
    pygame.display.flip()

pygame.quit()
sys.exit()