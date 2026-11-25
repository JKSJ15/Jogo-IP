import pygame

# desenho dos corações do jogador no canto da tela, representando as suas vidas no jogo
def desenhar_coracao(tela, x, y, tamanho, cor):
    r = tamanho // 4
    pygame.draw.circle(tela, cor, (x + r, y + r), r)
    pygame.draw.circle(tela, cor, (x + 3 * r, y + r), r)
    pygame.draw.polygon(tela, cor, [
        (x, y + r),
        (x + 4 * r, y + r),
        (x + 2 * r, y + 4 * r)
    ])