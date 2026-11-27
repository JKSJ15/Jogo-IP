import pygame
import random
from constantes import LARGURA_TELA, ALTURA_TELA, VERMELHO, BRANCO, VERDE
from uteis.pegarReacao import pegarReacao

class Letra(pegarReacao):
    # inicialização da letra
    def __init__(self, velocidade, texto, proibida=False):
        super().__init__()
        self.velocidade = velocidade
        self.texto = texto
        self.proibida = proibida

        # prepara o texto uma vez só 
        self.fonte = pygame.font.Font(None, 36)
        self.imagem_texto = self.fonte.render(self.texto, True, BRANCO)

        # tamanho do quadrado de acordo com a palavra (10px de folga de cada lado)
        self.largura = self.imagem_texto.get_width() + 20
        self.altura = 50

        # posição inicial: garante que a palavra inteira caiba na tela
        self.x = random.randint(0, max(0, LARGURA_TELA - self.largura))
        self.y = -self.altura

    # movimentação da letra
    def mover(self):
        self.y += self.velocidade

    # verifica se a letra já passou do fim da tela
    def saiu_da_tela(self):
        return self.y > ALTURA_TELA

    # desenhando a letra na tela
    def desenhar(self, tela):
        # proibida sera vermelho e permitida = verde
        if self.proibida:
            cor_fundo = VERMELHO
        else:
            cor_fundo = VERDE

        pygame.draw.rect(tela, cor_fundo, (self.x, self.y, self.largura, self.altura))

        rect_texto = self.imagem_texto.get_rect(
            center=(self.x + self.largura // 2, self.y + self.altura // 2)
        )
        tela.blit(self.imagem_texto, rect_texto)
    # pegando a reação da letra (área de colisão do tamanho do quadrado)
    def pegar_reacao(self):
        return pygame.Rect(self.x, self.y, self.largura, self.altura)