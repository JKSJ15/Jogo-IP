import pygame
import random
from constantes import LARGURA_TELA, ALTURA_TELA, VERMELHO

class Letra:
    def __init__(self, velocidade, texto):
        self.x = random.randint(0, LARGURA_TELA - 50)
        self.y = -50
        self.velocidade = velocidade
        self.texto = texto

    def mover(self):
        self.y += self.velocidade
        if self.y > ALTURA_TELA + 50:
            self.y = -50
            self.x = random.randint(0, LARGURA_TELA - 50)

    def desenhar(self, tela):
        pygame.draw.rect(tela, VERMELHO, (self.x, self.y, 50, 50))

        fonte = pygame.font.Font(None, 36)
        texto = fonte.render(self.texto, True, (255, 255, 255))

        rect_texto = texto.get_rect(center=(self.x + 25, self.y + 25))

        tela.blit(texto, rect_texto)

    def get_rect(self):
        return pygame.Rect(self.x, self.y, 50, 50)