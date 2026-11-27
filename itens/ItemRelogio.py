import pygame
import random
import math
from constantes import LARGURA_TELA, ALTURA_TELA, VERMELHO
from estilo.relogio import desenhar_relogio
from uteis.pegarReacao import pegarReacao

class ItemRelogio(pegarReacao):
    def __init__(self, velocidade):
        super().__init__()
        self.velocidade = velocidade
        self.tamanho = 44

        self.x = random.randint(0, LARGURA_TELA - self.tamanho)
        self.y = -self.tamanho

    # movimentação do item
    def mover(self):
        self.y += self.velocidade

    # verifica se o item já passou do fim da tela
    def saiu_da_tela(self):
        return self.y > ALTURA_TELA

    # desenhando o item: relógio pixelado balançando de lado
    def desenhar(self, tela):
        # o relógio é um sprite de pixels inteiros, então em vez de pulsar
        # (o que quebraria o tamanho dos pixels) ele balança de um lado pro outro
        balanco = int(math.sin(pygame.time.get_ticks() / 100) * 3)

        desenhar_relogio(tela, self.x + balanco, self.y, self.tamanho, VERMELHO)

    # área de colisão do item
    def pegar_reacao(self):
        return pygame.Rect(self.x, self.y, self.tamanho, self.tamanho)