import pygame
import random
from uteis.colisao import checar_colisao
from estilo.coracao import desenhar_coracao
from classes.Letras import Letra
from classes.ItemCoracao import ItemCoracao
from classes.ItemSapato import ItemSapato
from classes.Cenario import Cenario
from classes.Professor import Professor
from classes.Porta import Porta
from constantes import (
    VEL_LETRA_FASE1,
    VEL_LETRA_FASE2,
    VEL_LETRA_FASE3,
    PALAVRAS_FASE1,
    PALAVRAS_FASE2,
    PALAVRAS_FASE3,
    PROIBIDAS_FASE1,
    PROIBIDAS_FASE2,
    PROIBIDAS_FASE3,
    CHANCE_PROIBIDA,
    CHANCE_CORACAO,
    CHANCE_SAPATO,
    DURACAO_LENTIDAO,
    FATOR_LENTIDAO,
    VIDAS_MAXIMAS,
    VIDAS_INICIAIS,
    VERMELHO,
    CINZA,
    REINICIOS,
    INTERVALO_SPAWS,
    VEL_JOGADOR
)

class Fase:
    def __init__(self, numero_fase):
        self.numero_fase = numero_fase
        self.frases_coletadas = 0
        self.vidas = VIDAS_INICIAIS
        self.reinicios = REINICIOS
        self.letras = []
        self.coracoes = []
        self.sapatos = []
        self.fim_lentidao = 0
        self.velocidade_original = VEL_JOGADOR
        self.texto_aviso = ""
        self.tempo_aviso = 0
        self.ultimo_spawn = 0
        self.intervalo_spawn = INTERVALO_SPAWS
        self.cenario = Cenario()
        self.porta = Porta()

        # Configuração de cada fase
        if numero_fase == 1:
            self.meta_fase = 10
            self.velocidade_letras = VEL_LETRA_FASE1
            self.palavras = PALAVRAS_FASE1
            self.palavras_proibidas = PROIBIDAS_FASE1
            self.nome_sala = "E2"
            self.professor = Professor(480, 350, "STEFAN")

        elif numero_fase == 2:
            self.meta_fase = 20
            self.velocidade_letras = VEL_LETRA_FASE2
            self.palavras = PALAVRAS_FASE2
            self.palavras_proibidas = PROIBIDAS_FASE2
            self.nome_sala = "Grad5"
            self.professor = Professor(480, 350, "MARCIO")

        else:
            self.meta_fase = 30
            self.velocidade_letras = VEL_LETRA_FASE3
            self.palavras = PALAVRAS_FASE3
            self.palavras_proibidas = PROIBIDAS_FASE3
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
        self.vidas = VIDAS_INICIAIS
        self.letras = []
        self.coracoes = []
        self.sapatos = []
        self.texto_aviso = ""
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

    # desenha a barra do topo: contador de palavras + corações
    def desenhar_hud(self, tela):
        # fundo da barra
        pygame.draw.rect(tela, (20, 20, 40), (0, 0, tela.get_width(), 50))

        # contador de palavras coletadas
        texto = f"Palavras: {self.frases_coletadas}/{self.meta_fase}"
        self.desenhar_texto(tela, texto, self.fonte, 20, 15)

        # corações: vermelho = vida que ainda tem, cinza = vida perdida
        x_inicial = tela.get_width() - 40 * VIDAS_INICIAIS - 20
        for i in range(VIDAS_INICIAIS):
            if i < self.vidas:
                cor = VERMELHO
            else:
                cor = CINZA
            desenhar_coracao(tela, x_inicial + i * 40, 12, 28, cor)

    # inicia desafio
    def iniciar_desafio(self):
        self.estado = "desafio"
        self.letras = []
        self.coracoes = []
        self.sapatos = []
        self.texto_aviso = ""
        self.frases_coletadas = 0
        self.vidas = VIDAS_INICIAIS
        self.ultimo_spawn = pygame.time.get_ticks()

    # inicio da fase
    def iniciar(self, tela, teclas, jogador, eventos):
        avancar = False
        tela.fill((0, 0, 0))

        # se saiu do desafio (derrota, fase concluída...), a velocidade volta ao normal
        if self.estado != "desafio" and self.velocidade_original is not None:
            jogador.velocidade = self.velocidade_original
            self.velocidade_original = None
            self.sapatos = []

        # Desenhar cenário e atualizar a hitbox da porta
        self.cenario.desenhar(self.numero_fase, tela)
        self.porta.definir_area(self.cenario.porta_rect)

        # Verificar se E ou Q foi pressionado
        pressionou_e = any(evento.type == pygame.KEYDOWN and evento.key == pygame.K_e for evento in eventos)
        pressionou_q = any(evento.type == pygame.KEYDOWN and evento.key == pygame.K_q for evento in eventos)

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
                self.desenhar_texto(tela, "Pressione E para conversar", self.fonte, 350, 550, (0, 0, 0))
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

            # Gerar palavras, coração ou sapato aleatoriamente
            if tempo_atual - self.ultimo_spawn >= self.intervalo_spawn:
                sorteio = random.random()
                if sorteio < CHANCE_CORACAO:
                    self.coracoes.append(ItemCoracao(self.velocidade_letras))
                elif sorteio < CHANCE_CORACAO + CHANCE_SAPATO:
                    self.sapatos.append(ItemSapato(self.velocidade_letras))
                elif sorteio < CHANCE_CORACAO + CHANCE_SAPATO + CHANCE_PROIBIDA:
                    palavra = random.choice(self.palavras_proibidas)
                    self.letras.append(Letra(self.velocidade_letras, palavra, True))
                else:
                    palavra = random.choice(self.palavras)
                    self.letras.append(Letra(self.velocidade_letras, palavra, False))
                self.ultimo_spawn = tempo_atual

            # Movimentação e coleta das palavras
            for letra in self.letras[:]:
                if self.estado != "desafio":
                    continue

                letra.mover()
                letra.desenhar(tela)

                if checar_colisao(jogador, letra):
                    self.letras.remove(letra)

                    if letra.proibida:
                        # pegou palavra proibida: perde 1 vida
                        self.vidas -= 1
                        if self.vidas <= 0:
                            self.estado = "derrota"
                    else:
                        # pegou palavra permitida: conta ponto
                        self.frases_coletadas += 1
                        if self.frases_coletadas >= self.meta_fase:
                            self.estado = "concluida"
                            self.letras = []
                            self.coracoes = []
                            self.sapatos = []
                            self.ultimo_spawn = pygame.time.get_ticks()

                # palavra chegou no chão sem ninguém pegar: some
                elif letra.saiu_da_tela():
                    self.letras.remove(letra)

            # Movimentação e coleta dos corações
            for coracao in self.coracoes[:]:
                if self.estado != "desafio":
                    continue

                coracao.mover()
                coracao.desenhar(tela)

                if checar_colisao(jogador, coracao):
                    self.coracoes.remove(coracao)
                    # só ganha vida se tiver menos que o máximo (1 ou 2 vidas)
                    if self.vidas < VIDAS_MAXIMAS:
                        self.vidas += 1
                        self.texto_aviso = "+1 vida!"
                    else:
                        self.texto_aviso = "Vida cheia!"
                    self.tempo_aviso = tempo_atual

                # coração chegou no chão sem ninguém pegar: some
                elif coracao.saiu_da_tela():
                    self.coracoes.remove(coracao)

            # Movimentação e coleta dos sapatos (deixam o jogador lento)
            for sapato in self.sapatos[:]:
                if self.estado != "desafio":
                    continue

                sapato.mover()
                sapato.desenhar(tela)

                if checar_colisao(jogador, sapato):
                    self.sapatos.remove(sapato)

                    # guarda a velocidade normal só uma vez (para não acumular lentidão)
                    if self.velocidade_original is None:
                        self.velocidade_original = jogador.velocidade
                        jogador.velocidade = jogador.velocidade * FATOR_LENTIDAO

                    # pegar outro sapato renova o tempo
                    self.fim_lentidao = tempo_atual + DURACAO_LENTIDAO
                    self.texto_aviso = "Lento!"
                    self.tempo_aviso = tempo_atual

                # sapato chegou no chão sem ninguém pegar: some
                elif sapato.saiu_da_tela():
                    self.sapatos.remove(sapato)

            # acabou o tempo da lentidão, volta ao normal
            if self.velocidade_original is not None and tempo_atual >= self.fim_lentidao:
                jogador.velocidade = self.velocidade_original
                self.velocidade_original = None

            self.desenhar_hud(tela)

            # aviso embaixo dos corações do HUD por 1 segundo
            if self.texto_aviso != "" and tempo_atual - self.tempo_aviso < 1000:
                self.desenhar_texto(tela, self.texto_aviso, self.fonte, tela.get_width() - 160, 60, (255, 120, 120))

        # ESTADO 5: FASE CONCLUÍDA
        elif self.estado == "concluida":
            jogador.mover(teclas)
            self.porta.desenhar(tela, True)
            self.desenhar_texto(
                tela,
                "Fase concluída! Vá até a porta para continuar.",
                self.fonte,
                150,
                70,
                (0, 255, 0)
            )
            if checar_colisao(jogador, self.porta):
                avancar = True

        # ESTADO 5: DERROTA (acabaram as vidas)
        elif self.estado == "derrota":
            self.desenhar_hud(tela)
            self.desenhar_caixa(tela, "Você perdeu todas as vidas! (Q-sair, E-reiniciar)")

            if pressionou_e:
                if self.reinicios > 0:
                    self.reinicios -= 1
                    self.estado = "reiniciando"
                else:
                    self.estado = "morte"

            elif pressionou_q:
                self.frases_coletadas = 0
                self.vidas = VIDAS_INICIAIS
                self.indice_dialogo = 0
                self.estado = "exploracao"

        # ESTADO 6: REINICIANDO (usou reinicio)
        elif self.estado == "reiniciando":
            self.desenhar_hud(tela)
            self.desenhar_caixa(tela, f"Você possui {self.reinicios} reinícios restantes!")

            if pressionou_e:
                self.iniciar_desafio()

        # ESTADO 7: MORTE (sem mais reinícios)
        elif self.estado == "morte":
            self.desenhar_caixa(tela, "Você perdeu todas as vidas e reinícios! Jogo encerrado!")

            if pressionou_e:
                self.desenhar_caixa(tela, "Reprovação! Você ficará para sempre no CIn.")
                self.estado = "exploracao"
                self.frases_coletadas = 0
                self.vidas = VIDAS_INICIAIS
                self.reinicios = REINICIOS


        # Desenhar jogador por último
        jogador.desenhar(tela)
        return avancar