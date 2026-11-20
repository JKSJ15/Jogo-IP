import pygame
from constantes import AMARELO
from uteis.pegarReacao import pegarReacao

class Porta(pegarReacao):
    def __init__(self, x, y, largura, altura):
        super().__init__()
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura

    def desenhar(self, tela):
        pygame.draw.rect(tela, AMARELO, (self.x, self.y, self.largura, self.altura))