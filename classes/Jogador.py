import pygame
from constantes import COR_JOGADOR, LARGURA_TELA, ALTURA_TELA

class Jogador:
    # inicialização
    def __init__(self, x, y, velocidade):
        self.x = x
        self.y = y
        self.velocidade = velocidade

    # movimentação do jogador
    def mover(self, teclas):
        if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
            self.x -= self.velocidade
            if self.x < 0:
                self.x = 0
            elif self.x > LARGURA_TELA:
                self.x = LARGURA_TELA
        if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
            self.x += self.velocidade
            if self.x < 0:
                self.x = 0
            elif self.x > LARGURA_TELA:
                self.x = LARGURA_TELA
        if teclas[pygame.K_w] or teclas[pygame.K_UP]:
            self.y -= self.velocidade
            if self.y < 0:
                self.y = 0
            elif self.y > ALTURA_TELA:
                self.y = ALTURA_TELA
        if teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
            self.y += self.velocidade
            if self.y < 0:
                self.y = 0
            elif self.y > ALTURA_TELA:
                self.y = ALTURA_TELA

    # desenhar o jogador na tela
    def desenhar(self, tela):
        pygame.draw.circle(tela, COR_JOGADOR, (self.x, self.y), 25)
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, 50, 50)