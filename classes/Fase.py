import pygame
import random
from uteis.colisao import checar_colisao
from classes.Letras import Letra
from classes.Cenario import Cenario
from constantes import (VEL_LETRA, PALAVRAS_FASE1, PALAVRAS_FASE2, PALAVRAS_FASE3)

class Fase:
    def __init__(self, numero_fase):
        self.numero_fase = numero_fase
        self.frases_coletadas = 0
        self.letras = []
        self.ultimo_spawn = 0
        self.intervalo_spawn = 1500
        self.cenario = Cenario()

        # checando fase
        if numero_fase == 1:
            self.meta_fase = 10
            self.palavras = PALAVRAS_FASE1
        elif numero_fase == 2:
            self.meta_fase = 20
            self.palavras = PALAVRAS_FASE2
        else:
            self.meta_fase = 30
            self.palavras = PALAVRAS_FASE3

    def iniciar(self, tela, teclas, jogador):
        tela.fill((0, 0, 0))

        # Desenhar cenário correspondente
        if self.numero_fase == 1:
            self.cenario.desenharFase1(tela)
        elif self.numero_fase == 2:
            self.cenario.desenharFase2(tela)
        elif self.numero_fase == 3:
            self.cenario.desenharFase3(tela)

        # Movimentação do jogador
        jogador.mover(teclas)
        tempo_atual = pygame.time.get_ticks()

        # Gerar palavras aleatoriamente
        if tempo_atual - self.ultimo_spawn >= self.intervalo_spawn:
            palavra = random.choice(self.palavras)
            self.letras.append(
                Letra(VEL_LETRA, palavra)
            )
            self.ultimo_spawn = tempo_atual

        # Movimentação e coleta das letras
        for letra in self.letras[:]:
            letra.mover()
            letra.desenhar(tela)
            if checar_colisao(jogador, letra):
                self.frases_coletadas += 1
                self.letras.remove(letra)
                if self.frases_coletadas >= self.meta_fase:
                    return True

        # Desenhar jogador por último
        jogador.desenhar(tela)
        return False