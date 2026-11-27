import pygame

# desenho de um raio (por exemplo, para representar energia ou um power-up)
def desenhar_raio(tela, x, y, tamanho, cor):
    r = tamanho // 4
    pygame.draw.polygon(tela, cor, [
        (x + 3 * r, y),
        (x + r, y + 2 * r),
        (x + 2 * r, y + 2 * r),
        (x + r, y + 4 * r),
        (x + 3 * r, y + 2 * r),
        (x + 2 * r, y + 2 * r),
    ])