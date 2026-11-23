# CONFIGURAÇÕES GERAIS
FPS = 60

# Resolução da janela
NATIVE_W, NATIVE_H = 320, 240
SCALE = 3
LARGURA_TELA = NATIVE_W * SCALE # 960
ALTURA_TELA = NATIVE_H * SCALE # 720

# CORES GERAIS
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (50, 120, 255)
VERMELHO = (220, 50, 50)
AMARELO = (255, 255, 0)

# JOGADOR
COR_JOGADOR = (0, 255, 0)
X_JOGADOR = 432
Y_JOGADOR = 650
VEL_JOGADOR = 10

# LETRAS
VEL_LETRA = 5
PALAVRAS_FASE1 = [
    "ABRACAO", "AMOR", "PAZ", "FELICIDADE", "SAUDE"
]

PALAVRAS_FASE2 = [
    "LIBERDADE", "JUSTICA", "IGUALDADE", "PAZ", "FELICIDADE"
]

PALAVRAS_FASE3 = [
    "ESPERANCA", "AMIZADE", "LEALDADE", "CORAGEM", "SABEDORIA"
]

# UTILITÁRIOS
PASTA_IMAGENS = "assets/images"

# FASE 1
TILE = 16
COLS = 18
ROWS = 18
WIDTH = COLS * TILE
HEIGHT = ROWS * TILE
PALETTE_FASE1 = {
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

# FASE 2
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

C_GLASS_BG = (212, 229, 242)
C_GLASS_SHADE = (184, 206, 224)
C_GLASS_SHINE = (245, 251, 255)
C_METAL = (130, 140, 152)

C_BLUE_LIGHT = (122, 182, 248)
C_BLUE_MID = (64, 134, 222)
C_BLUE_DARK = (36, 84, 158)
C_BLUE_DEEP = (24, 56, 112)

# FASE3
# Resolução interna estilo GBA (pixel art) e janela escalada 3x
INTERNAL_W, INTERNAL_H = 320, 240
SCALE = 3
SCREEN_W, SCREEN_H = INTERNAL_W * SCALE, INTERNAL_H * SCALE