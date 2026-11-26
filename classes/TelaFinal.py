import pygame
import random
import math
from constantes import LARGURA_TELA, ALTURA_TELA, BRANCO, AMARELO, VERMELHO

CORES_CONFETE = [(255, 80, 80), (255, 200, 60), (80, 200, 120), (80, 160, 255), (200, 100, 255)]
PALAVRAS_DERROTA = ["BREAK", "NONE", "XOR", "NAND", "NIVAN", "GLOBAL", "CONTINUE"]


class TelaFinal:
    def __init__(self, tipo, info=""):
        self.tipo = tipo          # Representa a vitoria ou derrota do jogador
        self.info = info          
        self.opcoes = ["Jogar de novo", "Sair"]
        self.selecionada = 0
        self.tempo_inicio = pygame.time.get_ticks()

        # Fontes
        self.fonte_titulo = pygame.font.Font(None, 100)
        self.fonte_texto = pygame.font.Font(None, 34)
        self.fonte_opcao = pygame.font.Font(None, 40)
        self.fonte_pequena = pygame.font.Font(None, 24)

        # Botões
        self.botoes = []
        largura = 320
        altura = 60
        x = (LARGURA_TELA - largura) // 2
        for i in range(len(self.opcoes)):
            self.botoes.append(pygame.Rect(x, 420 + i * 85, largura, altura))

        # Partículas: confetes na vitória, palavras proibidas caindo na derrota
        if self.tipo == "vitoria":
            quantidade = 80
        else:
            quantidade = 25
        self.particulas = []
        for i in range(quantidade):
            self.particulas.append(self.criar_particula(random.randint(-ALTURA_TELA, ALTURA_TELA)))

    # cria uma partícula na altura y
    def criar_particula(self, y):
        particula = {
            "x": random.randint(0, LARGURA_TELA),
            "y": y,
            "vel": random.uniform(1.5, 4),
            "balanco": random.uniform(0, 6.28),
        }
        if self.tipo == "vitoria":
            particula["cor"] = random.choice(CORES_CONFETE)
            particula["tam"] = random.randint(6, 12)
        else:
            particula["texto"] = random.choice(PALAVRAS_DERROTA)
        return particula

    # move e desenha as partículas
    def atualizar_particulas(self, tela):
        for p in self.particulas:
            p["y"] += p["vel"]
            p["balanco"] += 0.05
            x = p["x"] + math.sin(p["balanco"]) * 15

            if self.tipo == "vitoria":
                pygame.draw.rect(tela, p["cor"], (x, p["y"], p["tam"], p["tam"] // 2))
            else:
                imagem = self.fonte_pequena.render(p["texto"], True, (110, 55, 60))
                tela.blit(imagem, (x, p["y"]))

            # saiu por baixo: volta lá pra cima
            if p["y"] > ALTURA_TELA:
                p["y"] = random.randint(-100, -20)
                p["x"] = random.randint(0, LARGURA_TELA)

    # título pulsando + subtítulo
    def desenhar_titulo(self, tela, tempo):
        if self.tipo == "vitoria":
            texto = "APROVADO!"
            cor = AMARELO
            subtitulo = "Parabéns! Você sobreviveu ao CIn!"
        else:
            texto = "REPROVADO!"
            cor = VERMELHO
            subtitulo = "Você ficará para sempre no CIn..."

        escala = 1 + math.sin(tempo / 250) * 0.06
        imagem = self.fonte_titulo.render(texto, True, cor)
        imagem = pygame.transform.rotozoom(imagem, 0, escala)
        tela.blit(imagem, imagem.get_rect(center=(LARGURA_TELA // 2, 170)))

        sub = self.fonte_texto.render(subtitulo, True, BRANCO)
        tela.blit(sub, sub.get_rect(center=(LARGURA_TELA // 2, 260)))

        if self.info != "":
            info = self.fonte_texto.render(self.info, True, (200, 200, 200))
            tela.blit(info, info.get_rect(center=(LARGURA_TELA // 2, 305)))

    # botões; o selecionado fica amarelo
    def desenhar_botoes(self, tela):
        for i in range(len(self.botoes)):
            rect = self.botoes[i]
            if i == self.selecionada:
                cor_fundo = (60, 60, 110)
                cor_borda = AMARELO
            else:
                cor_fundo = (25, 25, 45)
                cor_borda = BRANCO
            pygame.draw.rect(tela, cor_fundo, rect, border_radius=12)
            pygame.draw.rect(tela, cor_borda, rect, 3, border_radius=12)
            imagem = self.fonte_opcao.render(self.opcoes[i], True, cor_borda)
            tela.blit(imagem, imagem.get_rect(center=rect.center))

        dica = self.fonte_pequena.render(
            "Setas ou W/S para escolher  -  ENTER ou E para confirmar", True, (170, 170, 170)
        )
        tela.blit(dica, dica.get_rect(center=(LARGURA_TELA // 2, ALTURA_TELA - 30)))

    # devolve "reiniciar" ou "sair" conforme o botão selecionado
    def escolher(self):
        if self.selecionada == 0:
            return "reiniciar"
        return "sair"

    # roda a tela final; devolve "", "reiniciar" ou "sair"
    def atualizar(self, tela, eventos):
        acao = ""
        tempo = pygame.time.get_ticks() - self.tempo_inicio

        if self.tipo == "vitoria":
            tela.fill((15, 25, 60))
        else:
            tela.fill((40, 10, 15))

        self.atualizar_particulas(tela)
        self.desenhar_titulo(tela, tempo)
        self.desenhar_botoes(tela)

        # espera 0,8 s antes de aceitar comandos, pra ninguém confirmar sem querer
        if tempo >= 800:
            for evento in eventos:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                        self.selecionada = (self.selecionada - 1) % len(self.opcoes)
                    elif evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                        self.selecionada = (self.selecionada + 1) % len(self.opcoes)
                    elif evento.key == pygame.K_RETURN or evento.key == pygame.K_e:
                        acao = self.escolher()

                # mouse em cima de um botão seleciona ele
                elif evento.type == pygame.MOUSEMOTION:
                    for i in range(len(self.botoes)):
                        if self.botoes[i].collidepoint(evento.pos):
                            self.selecionada = i

                # clique com o botão esquerdo confirma
                elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    for i in range(len(self.botoes)):
                        if self.botoes[i].collidepoint(evento.pos):
                            self.selecionada = i
                            acao = self.escolher()

        return acao