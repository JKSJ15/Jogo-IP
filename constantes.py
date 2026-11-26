# CONFIGURAÇÕES GERAIS
FPS = 60

# RESOLUÇÃO DA JANELA
NATIVE_W = 320
NATIVE_H = 240
SCALE = 3

LARGURA_TELA = NATIVE_W * SCALE
ALTURA_TELA = NATIVE_H * SCALE

# RESOLUÇÃO DOS CENÁRIOS
TILE = 16
COLS = 18
ROWS = 18

WIDTH = COLS * TILE
HEIGHT = ROWS * TILE

# CORES GERAIS
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (50, 120, 255)
VERMELHO = (220, 50, 50)
AMARELO = (255, 255, 0)
CINZA = (90, 90, 90)

# JOGADOR
COR_JOGADOR = (0, 255, 0)
X_JOGADOR = 432
Y_JOGADOR = 650
VEL_JOGADOR = 10
REINICIOS = 1
VIDAS_INICIAIS = 3

# LETRAS
VEL_LETRA = 5
INTERVALO_SPAWS = 500
PALAVRAS_FASE1 = [
    "ABRACAO", "AMOR", "PAZ", "FELICIDADE", "SAUDE"
]

PALAVRAS_FASE2 = [
    "LIBERDADE", "JUSTICA", "IGUALDADE", "PAZ", "FELICIDADE"
]

PALAVRAS_FASE3 = [
    "ESPERANCA", "AMIZADE", "LEALDADE", "CORAGEM", "SABEDORIA"
]

# PALAVRAS PROIBIDAS (tiram 1 vida)
PROIBIDAS_FASE1 = [
    "X-BARRADO", "XOR", "NOR", "AND", "NAND"
]

PROIBIDAS_FASE2 = [
    "BREAK", "NONE", "GLOBAL", "CONTINUE", "SETS"
]

PROIBIDAS_FASE3 = [
    "NIVAN", "NIVAN", "NIVAN", "NIVAN", "NIVAN"
]

# Chance de uma palavra que cai ser proibida (0.3 = 30%)
CHANCE_PROIBIDA = 0.3

# Chance de cair um coração (0.08 = 8%) e máximo de vidas
CHANCE_CORACAO = 0.08
VIDAS_MAXIMAS = 3

# Chance de cair um coração (0.08 = 8%) e duração da lentidão (4 segundos)
CHANCE_SAPATO = 0.08
DURACAO_LENTIDAO = 4000
FATOR_LENTIDAO = 0.5

# UTILITÁRIOS
PASTA_IMAGENS = "assets/images"

# FASE 2 (Grad 5)
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

# FASE 1 (E2)
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

# RESOLUÇÃO FASE 3
INTERNAL_W = WIDTH
INTERNAL_H = HEIGHT

# PROFESSORES

DIALOGO_FASE1 = [
    "Olá, boah tardih!",
    "Aqui é onde você iniciará sua jornada",
    "Hojê studaremos Verrilog e portas lóghicas",
    "Pegue apenas as portas lóghicas, evite outras palavras",
    "so, vamos coméçar, boa sorthi!"
    ]
DIALOGO_FASE2 = [
    "Olá, meu nome é Márcio, seja bem-vindo à sala Grad 5!",
    "Você deve fazer um desafio para conseguir a aprovação e sair daqui",
    "Você deverá coletar os comandos permitidos e evitar os proibidos",
    "Caso pegue mais de 3 proibidos, reprovará e ficará para sempre aqui",
    "Bom desafio! Talvez não tão bom..."]


DIALOGO_FASE3 = [
    "Olá, Tablito! Achou que seria fácil assim?",
    "Para conseguir aprovação e conseguir sair daqui, terá que passar por mim", 
    "O temido Nivan",
    "te garanto que não será tão fácil assim...",
    "Enfrente chuvas de assuntos e evite distrações",
    "Bom desafio, aguardo sua reprovação!"
    ]