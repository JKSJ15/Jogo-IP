import pygame

# mapa do sapato: O = contorno, C = corpo, S = sola, D = detalhe, . = vazio
MAPA_SAPATO = [
    "....OOOO....",
    "....OCCO....",
    "....OCCO....",
    "....ODCO....",
    "....OCDO....",
    "....OCCOOO..",
    "....OCCCCCO.",
    "..OOOCCCCCCO",
    ".OCCCCCCCCCO",
    "OCCCCCCCCCCO",
    "OSSSSSSSSSSO",
    ".OOOOOOOOOO.",
]

CORES_SAPATO = {
    "O": (30, 30, 30),
    "C": (200, 40, 40),
    "S": (240, 240, 240),
    "D": (255, 255, 255),
}

# desenho do sapato pixelado, igual ao desenhar_coracao
def desenhar_sapato(tela, x, y, tamanho):
    p = tamanho // 12  # tamanho de cada "pixel"
    for linha, texto in enumerate(MAPA_SAPATO):
        for coluna, letra in enumerate(texto):
            if letra in CORES_SAPATO:
                pygame.draw.rect(
                    tela, CORES_SAPATO[letra],
                    (x + coluna * p, y + linha * p, p, p)
                )