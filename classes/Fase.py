import pygame
import random
from uteis.colisao import checar_colisao
from classes.Letras import Letra
from classes.Cenario import Cenario
from classes.Professor import Professor
from constantes import (
    VEL_LETRA,
    PALAVRAS_FASE1,
    PALAVRAS_FASE2,
    PALAVRAS_FASE3
)

class Fase:
    def __init__(self, numero_fase):
        self.numero_fase = numero_fase
        self.frases_coletadas = 0
        self.letras = []
        self.ultimo_spawn = 0
        self.intervalo_spawn = 1500
        self.cenario = Cenario()

        # Configuração de cada fase
        if numero_fase == 1:
            self.meta_fase = 10
            self.palavras = PALAVRAS_FASE1
            self.nome_sala = "Grad5"
            self.professor = Professor(480, 350, "MARCIO")

        elif numero_fase == 2:
            self.meta_fase = 20
            self.palavras = PALAVRAS_FASE2
            self.nome_sala = "E2"
            self.professor = Professor(480, 350, "STEFAN")

        else:
            self.meta_fase = 30
            self.palavras = PALAVRAS_FASE3
            self.nome_sala = "E1"
            self.professor = Professor(480, 350, "NAVIN")

        # Controle dos estados
        self.estado = "entrada"
        self.tempo_entrada = pygame.time.get_ticks()
        self.dialogos = []
        self.indice_dialogo = 0

        # Fontes
        self.fonte = pygame.font.Font(None, 30)
        self.fonte_pequena = pygame.font.Font(None, 24)

    # reinicia a fase
    def reiniciar(self):
        self.estado = "entrada"
        self.tempo_entrada = pygame.time.get_ticks()
        self.frases_coletadas = 0
        self.letras = []
        self.dialogos = []
        self.indice_dialogo = 0
        self.ultimo_spawn = pygame.time.get_ticks()

    # desenha texto na tela
    def desenhar_texto(self, tela, texto, fonte, x, y, cor=(255, 255, 255)):
        imagem = fonte.render(texto, True, cor)
        tela.blit(imagem, (x, y))

    # desenha caixa de texto
    def desenhar_caixa(self, tela, texto):
        largura = 700
        altura = 100
        x = (tela.get_width() - largura) // 2
        y = tela.get_height() - altura - 25
        pygame.draw.rect(tela, (20, 20, 40), (x, y, largura, altura), border_radius=10)
        pygame.draw.rect(tela, (255, 255, 255), (x, y, largura, altura), 3, border_radius=10)
        self.desenhar_texto(tela, texto, self.fonte, x + 20, y + 25)
        self.desenhar_texto(tela, "Pressione E", self.fonte_pequena, x + largura - 140, y + 70, (255, 220, 100))

    # desenha nome da tela ao iniciar
    def desenhar_nome_sala(self, tela):
        largura = 400
        altura = 60
        x = (tela.get_width() - largura) // 2
        y = 80
        pygame.draw.rect(tela, (20, 20, 40), (x, y, largura, altura), border_radius=10)
        pygame.draw.rect(tela, (255, 255, 255), (x, y, largura, altura), 2, border_radius=10)
        texto = self.fonte.render(self.nome_sala, True, (255, 255, 255))
        tela.blit(texto, texto.get_rect(center=(tela.get_width() // 2, y + altura // 2)))

    # inicia desafio
    def iniciar_desafio(self):
        self.estado = "desafio"
        self.letras = []
        self.ultimo_spawn = pygame.time.get_ticks()

    # inicio da fase
    def iniciar(self, tela, teclas, jogador, eventos):
        tela.fill((0, 0, 0))

        # Desenhar cenário
        if self.numero_fase == 1:
            self.cenario.desenharFase1(tela)
        elif self.numero_fase == 2:
            self.cenario.desenharFase2(tela)
        elif self.numero_fase == 3:
            self.cenario.desenharFase3(tela)

        # Verificar se E foi pressionado
        pressionou_e = any(evento.type == pygame.KEYDOWN and evento.key == pygame.K_e for evento in eventos)

        # ESTADO 1: ENTRADA
        if self.estado == "entrada":
            self.desenhar_nome_sala(tela)
            tempo_atual = pygame.time.get_ticks()
            if tempo_atual - self.tempo_entrada >= 2000:
                self.estado = "exploracao"

        # ESTADO 2: EXPLORAÇÃO
        elif self.estado == "exploracao":
            jogador.mover(teclas)
            self.professor.desenhar(tela)
            if checar_colisao(jogador, self.professor):
                self.desenhar_texto(tela, "Pressione E para conversar", self.fonte, 350, 550, (255, 255, 0))
                if pressionou_e:
                    self.dialogos = self.professor.dialogar()

                    # Garante que o diálogo seja uma lista
                    if isinstance(self.dialogos, str):
                        self.dialogos = [self.dialogos]

                    self.indice_dialogo = 0
                    self.estado = "dialogo"

        # ESTADO 3: DIÁLOGO
        elif self.estado == "dialogo":
            self.professor.desenhar(tela)
            if self.indice_dialogo < len(self.dialogos):
                self.desenhar_caixa(tela, self.dialogos[self.indice_dialogo])
                if pressionou_e:
                    self.indice_dialogo += 1
                    # Verifica se terminou todas as falas
                    if self.indice_dialogo >= len(self.dialogos):
                        self.estado = "desafio"

        # ESTADO 4: DESAFIO
        elif self.estado == "desafio":
            jogador.mover(teclas)
            tempo_atual = pygame.time.get_ticks()

            # Gerar palavras aleatoriamente
            if tempo_atual - self.ultimo_spawn >= self.intervalo_spawn:
                palavra = random.choice(self.palavras)
                self.letras.append(Letra(VEL_LETRA, palavra))
                self.ultimo_spawn = tempo_atual

            # Movimentação e coleta
            for letra in self.letras[:]:
                letra.mover()
                letra.desenhar(tela)

                if checar_colisao(jogador, letra):
                    self.frases_coletadas += 1
                    self.letras.remove(letra)
                    if self.frases_coletadas >= self.meta_fase:
                        jogador.desenhar(tela)
                        return True

        # Desenhar jogador por último
        jogador.desenhar(tela)
        return False