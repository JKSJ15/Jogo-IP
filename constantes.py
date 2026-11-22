# exibição / informações da tela
LARGURA_TELA = 800
ALTURA_TELA = 800
FPS = 60

# cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (50, 120, 255)
VERMELHO = (220, 50, 50)
AMARELO = (255, 255, 0)

# jogador
COR_JOGADOR = (0, 255, 0)
X_JOGADOR = 432
Y_JOGADOR = 750
VEL_JOGADOR = 10

#letras
VEL_LETRA = 5
PALAVRAS_FASE1 = ["ABRACAO", "AMOR", "PAZ", "FELICIDADE", "SAUDE"]
PALAVRAS_FASE2 = ["LIBERDADE", "JUSTICA", "IGUALDADE", "PAZ", "FELICIDADE"]
PALAVRAS_FASE3 = ["ESPERANCA", "AMIZADE", "LEALDADE", "CORAGEM", "SABEDORIA"]

# uteis
PASTA_IMAGENS = "assets/images"

# FASE 1
# Configurações do cenário
TILE = 16
SCALE = 3
COLS = 18
ROWS = 18

WIDTH = COLS * TILE
HEIGHT = ROWS * TILE
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