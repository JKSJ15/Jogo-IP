import pygame
from constantes import AMARELO
from uteis.pegarReacao import pegarReacao

class Porta(pegarReacao):
    def __init__(self, x=0, y=0, largura=0, altura=0):
        super().__init__()
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura

    def definir_area(self, rect):
        # x, y = centro da hitbox (para bater com o checar_colisao)
        self.x, self.y = rect.centerx, rect.centery
        self.largura, self.altura = rect.w, rect.h

    def desenhar(self, tela, debug=False):
        if debug:
            pygame.draw.rect(
                tela, AMARELO,
                (self.x - self.largura // 2, self.y - self.altura // 2,
                self.largura, self.altura),
                2
            )