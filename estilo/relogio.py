import pygame

# desenho de um relógio pixelado, estilo Pokémon (sprite 11x11)
def desenhar_relogio(tela, x, y, tamanho, cor):
    p = tamanho // 11  # tamanho de cada "pixel" do sprite

    contorno = (40, 40, 40)
    rosto = (248, 248, 248)
    marcas = (150, 150, 150)

    # O = contorno | F = rosto | H = ponteiros | T = marcação das horas | . = vazio
    sprite = [
        "...OOOOO...",
        ".OOFFTFFOO.",
        ".OFFFHFFFO.",
        "OFFFFHFFFFO",
        "OFFFFHFFFFO",
        "OTFFFHHHFTO",
        "OFFFFFFFFFO",
        "OFFFFFFFFFO",
        ".OFFFFFFFO.",
        ".OOFFTFFOO.",
        "...OOOOO...",
    ]

    cores = {
        "O": contorno,
        "F": rosto,
        "H": cor,
        "T": marcas,
    }

    for linha, texto in enumerate(sprite):
        for coluna, letra in enumerate(texto):
            if letra in cores:
                pygame.draw.rect(
                    tela,
                    cores[letra],
                    (x + coluna * p, y + linha * p, p, p)
                )