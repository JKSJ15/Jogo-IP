import pygame
import random
import math
from constantes import LARGURA_TELA, ALTURA_TELA
from estilo.sapato import desenhar_sapato
from uteis.pegarReacao import pegarReacao

class ItemSapato(pegarReacao):
    def __init__(self, velocidade):
        super().__init__()
        self.velocidade = velocidade
        self.tamanho = 48  # múltiplo de 12 para os pixels ficarem certinhos

        self.x = random.randint(0, LARGURA_TELA - self.tamanho)
        self.y = -self.tamanho

    # movimentação do item
    def mover(self):
        self.y += self.velocidade

    # verifica se o item já passou do fim da tela
    def saiu_da_tela(self):
        return self.y > ALTURA_TELA

    # desenhando o item: sapato balançando de leve
    def desenhar(self, tela):
        balanco = int(math.sin(pygame.time.get_ticks() / 150) * 3)
        desenhar_sapato(tela, self.x, self.y + balanco, self.tamanho)

    # área de colisão do item
    def pegar_reacao(self):
        return pygame.Rect(self.x, self.y, self.tamanho, self.tamanho)