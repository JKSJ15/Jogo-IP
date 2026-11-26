import pygame
import random
import math
from constantes import LARGURA_TELA, ALTURA_TELA, VERMELHO
from uteis.coracao import desenhar_coracao
from uteis.pegarReacao import pegarReacao

class ItemCoracao(pegarReacao):
    def __init__(self, velocidade):
        super().__init__()
        self.velocidade = velocidade
        self.tamanho = 40 

        self.x = random.randint(0, LARGURA_TELA - self.tamanho)
        self.y = -self.tamanho

    # movimentação do item
    def mover(self):
        self.y += self.velocidade

    # verifica se o item já passou do fim da tela
    def saiu_da_tela(self):
        return self.y > ALTURA_TELA

    # desenhando o item: só o coração, com borda escura, pulsando
    def desenhar(self, tela):
        centro_x = self.x + self.tamanho // 2
        centro_y = self.y + self.tamanho // 2

        # o coração aumenta e diminui um pouquinho pra chamar atenção
        pulso = int(math.sin(pygame.time.get_ticks() / 150) * 2)
        tamanho_coracao = 32 + pulso
        x_coracao = centro_x - tamanho_coracao // 2
        y_coracao = centro_y - tamanho_coracao // 2

        # borda escura (um coração um pouco maior por trás)
        borda = 4                                                                                         
        desenhar_coracao(tela, x_coracao - borda, y_coracao - borda, tamanho_coracao + 2 * borda, (40, 20, 25))

        desenhar_coracao(tela, x_coracao, y_coracao, tamanho_coracao, VERMELHO)

    # área de colisão do item
    def pegar_reacao(self):
        return pygame.Rect(self.x, self.y, self.tamanho, self.tamanho)