import pygame
import random
from constantes import LARGURA_TELA, ALTURA_TELA, VERMELHO
from uteis.pegarReacao import pegarReacao

class Letra(pegarReacao):
    # inicialização da letra
    def __init__(self, velocidade, texto):
        super().__init__()
        self.x = random.randint(0, LARGURA_TELA - 50)
        self.y = -50
        self.velocidade = velocidade
        self.texto = texto

    # movimentação da letra
    def mover(self):
        self.y += self.velocidade
        if self.y > ALTURA_TELA + 50:
            self.y = -50
            self.x = random.randint(0, LARGURA_TELA - 50)

    # desenhando a letra na tela
    def desenhar(self, tela):
        pygame.draw.rect(tela, VERMELHO, (self.x, self.y, 50, 50))

        fonte = pygame.font.Font(None, 36)
        texto = fonte.render(self.texto, True, (255, 255, 255))

        rect_texto = texto.get_rect(center=(self.x + 25, self.y + 25))

        tela.blit(texto, rect_texto)

    # pegando a reação da letra
    def pegar_reacao(self):
        return pygame.Rect(self.x, self.y, 50, 50)