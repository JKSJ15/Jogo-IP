import pygame
import random
import math
from constantes import (
    LARGURA_TELA,
    ALTURA_TELA,
    BRANCO,
    AMARELO,
    PALAVRAS_FASE1,
    PALAVRAS_FASE2,
    PALAVRAS_FASE3,
    PROIBIDAS_FASE1,
    PROIBIDAS_FASE2
)

# palavras que ficam caindo no fundo da tela inicial
PALAVRAS_PERMITIDAS = PALAVRAS_FASE1 + PALAVRAS_FASE2 + PALAVRAS_FASE3
PALAVRAS_PROIBIDAS = PROIBIDAS_FASE1 + PROIBIDAS_FASE2 + ["NIVAN"]

# cores das palavras: (normal, acesa quando o mouse chega perto)
CORES_PERMITIDA = ((60, 120, 85), (120, 255, 150))
CORES_PROIBIDA = ((125, 55, 65), (255, 90, 90))

RAIO_MOUSE = 130  # distância em que o mouse empurra as palavras


class TelaInicial:
    def __init__(self):
        self.opcoes = ["Iniciar", "Sair"]
        self.selecionada = 0
        self.tempo_inicio = pygame.time.get_ticks()
        self.mouse = (LARGURA_TELA // 2, ALTURA_TELA // 2)

        # Fontes
        self.fonte_titulo = pygame.font.Font(None, 120)
        self.fonte_subtitulo = pygame.font.Font(None, 36)
        self.fonte_opcao = pygame.font.Font(None, 44)
        self.fonte_palavra = pygame.font.Font(None, 30)
        self.fonte_pequena = pygame.font.Font(None, 24)

        # Botões
        self.botoes = []
        largura = 320
        altura = 60
        x = (LARGURA_TELA - largura) // 2
        for i in range(len(self.opcoes)):
            self.botoes.append(pygame.Rect(x, 430 + i * 85, largura, altura))

        # Fundo em degradê (desenhado uma vez só)
        self.fundo = pygame.Surface((LARGURA_TELA, ALTURA_TELA))
        for y in range(ALTURA_TELA):
            t = y / ALTURA_TELA
            cor = (int(10 + 25 * t), int(12 + 8 * t), int(35 + 30 * t))
            pygame.draw.line(self.fundo, cor, (0, y), (LARGURA_TELA, y))

        # Faixa escura atrás do título, pra ele não se misturar com as palavras
        self.faixa = pygame.Surface((LARGURA_TELA, 230), pygame.SRCALPHA)
        self.faixa.fill((0, 0, 0, 120))

        # Estrelas piscando
        self.estrelas = []
        for i in range(90):
            self.estrelas.append({
                "x": random.randint(0, LARGURA_TELA),
                "y": random.randint(0, ALTURA_TELA),
                "tam": random.randint(1, 3),
                "fase": random.uniform(0, 6.28),
            })

        # Palavras caindo
        self.palavras = []
        for i in range(22):
            self.palavras.append(self.criar_palavra(random.randint(-ALTURA_TELA, ALTURA_TELA)))

    # cria uma palavra na altura y (30% de chance de ser proibida)
    def criar_palavra(self, y):
        proibida = random.random() < 0.3
        if proibida:
            texto = random.choice(PALAVRAS_PROIBIDAS)
            cores = CORES_PROIBIDA
        else:
            texto = random.choice(PALAVRAS_PERMITIDAS)
            cores = CORES_PERMITIDA

        return {
            "x": random.randint(20, LARGURA_TELA - 120),
            "y": y,
            "vel": random.uniform(1, 2.5),
            "desvio": 0,
            "imagem": self.fonte_palavra.render(texto, True, cores[0]),
            "imagem_acesa": self.fonte_palavra.render(texto, True, cores[1]),
        }

    # estrelas piscam e se mexem um pouquinho seguindo o mouse
    def desenhar_estrelas(self, tela, tempo):
        mx = (self.mouse[0] - LARGURA_TELA // 2) * 0.02
        my = (self.mouse[1] - ALTURA_TELA // 2) * 0.02
        for e in self.estrelas:
            brilho = int(150 + 100 * math.sin(tempo / 400 + e["fase"]))
            x = e["x"] - mx * e["tam"]
            y = e["y"] - my * e["tam"]
            pygame.draw.circle(tela, (brilho, brilho, brilho), (int(x), int(y)), e["tam"])

    # palavras caem; perto do mouse elas são empurradas pro lado e acendem
    def atualizar_palavras(self, tela):
        for p in self.palavras:
            p["y"] += p["vel"]

            centro_x = p["x"] + p["desvio"] + p["imagem"].get_width() // 2
            dx = centro_x - self.mouse[0]
            dy = p["y"] - self.mouse[1]
            distancia = math.hypot(dx, dy)

            perto = distancia < RAIO_MOUSE
            if perto and distancia > 0:
                forca = (RAIO_MOUSE - distancia) / RAIO_MOUSE
                p["desvio"] += dx / distancia * forca * 6

            # volta devagar pro lugar quando o mouse se afasta
            p["desvio"] *= 0.93

            if perto:
                imagem = p["imagem_acesa"]
            else:
                imagem = p["imagem"]
            tela.blit(imagem, (p["x"] + p["desvio"], p["y"]))

            # saiu por baixo: volta lá pra cima como uma palavra nova
            if p["y"] > ALTURA_TELA:
                nova = self.criar_palavra(random.randint(-120, -30))
                p.update(nova)

    # título balançando, com sombra, e subtítulo
    def desenhar_titulo(self, tela, tempo):
        tela.blit(self.faixa, (0, 80))

        y = 170 + math.sin(tempo / 500) * 8
        escala = 1 + math.sin(tempo / 300) * 0.03

        sombra = self.fonte_titulo.render("VAMOS CINBORA", True, (0, 0, 0))
        sombra = pygame.transform.rotozoom(sombra, 0, escala)
        tela.blit(sombra, sombra.get_rect(center=(LARGURA_TELA // 2 + 5, y + 5)))

        titulo = self.fonte_titulo.render("VAMOS CINBORA", True, AMARELO)
        titulo = pygame.transform.rotozoom(titulo, 0, escala)
        tela.blit(titulo, titulo.get_rect(center=(LARGURA_TELA // 2, y)))

        sub = self.fonte_subtitulo.render("Sobreviva ao CIn e conquiste a aprovação!", True, BRANCO)
        tela.blit(sub, sub.get_rect(center=(LARGURA_TELA // 2, 260)))

    # botões; o selecionado fica amarelo e pulsa
    def desenhar_botoes(self, tela, tempo):
        for i in range(len(self.opcoes)):
            rect = self.botoes[i]
            if i == self.selecionada:
                cor_fundo = (60, 60, 110)
                cor_borda = AMARELO
                crescer = int(4 + math.sin(tempo / 200) * 4)
                rect = rect.inflate(crescer, crescer)
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

    # devolve a ação da opção escolhida
    def escolher(self):
        if self.selecionada == 0:
            return "iniciar"
        return "sair"

    # roda a tela inicial; devolve "", "iniciar" ou "sair"
    def atualizar(self, tela, eventos):
        acao = ""
        tempo = pygame.time.get_ticks() - self.tempo_inicio

        tela.blit(self.fundo, (0, 0))
        self.desenhar_estrelas(tela, tempo)
        self.atualizar_palavras(tela)
        self.desenhar_titulo(tela, tempo)
        self.desenhar_botoes(tela, tempo)

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
                self.mouse = evento.pos
                for i in range(len(self.opcoes)):
                    if self.botoes[i].collidepoint(evento.pos):
                        self.selecionada = i

            # clique com o botão esquerdo confirma
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                for i in range(len(self.opcoes)):
                    if self.botoes[i].collidepoint(evento.pos):
                        self.selecionada = i
                        acao = self.escolher()

        return acao