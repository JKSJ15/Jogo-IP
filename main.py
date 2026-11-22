import pygame
from classes.Jogador import Jogador
from classes.Porta import Porta
from classes.Fase import Fase
from uteis.colisao import checar_colisao
from constantes import (LARGURA_TELA, ALTURA_TELA, FPS, VEL_JOGADOR, X_JOGADOR, Y_JOGADOR)

def main():
    # inicia e configura o pygame
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    clock = pygame.time.Clock()

    # Instanciando Objetos do Jogo
    # Jogador
    jogador = Jogador(X_JOGADOR, Y_JOGADOR, VEL_JOGADOR)
    
    # Portas do menu
    porta1 = Porta(100, 200, 100, 150)
    porta2 = Porta(350, 200, 100, 150)
    porta3 = Porta(600, 200, 100, 150)

    # Fases
    fase1 = Fase(1)
    fase2 = Fase(2)
    fase3 = Fase(3)

    # looping principal do jogo
    fase_escolhida = None
    venceu = False
    rodando = True
    while rodando:
        # verificar saida do jogo
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        # pegar teclas pressionadas
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_ESCAPE]:
            rodando = False

        # renderizar a tela
        tela.fill((30, 30, 30))

        # MENU DE SELEÇÃO - não escolheu fase
        if fase_escolhida is None:

            # desenhando Portas
            porta1.desenhar(tela)
            porta2.desenhar(tela)
            porta3.desenhar(tela)

            # movimentação e criação do jogador
            jogador.mover(teclas)
            jogador.desenhar(tela)

            # Escolha da fase pela colisão
            if checar_colisao(jogador, porta1):
                fase_escolhida = fase1

            elif checar_colisao(jogador, porta2):
                fase_escolhida = fase2

            elif checar_colisao(jogador, porta3):
                fase_escolhida = fase3

            # Reiniciar posição do jogador ao escolher
            if fase_escolhida is not None:
                jogador.x = X_JOGADOR
                jogador.y = Y_JOGADOR

        # EXECUTAR FASE ESCOLHIDA - após seleção de fase
        else:
            # Verificar conclusão da fase
            venceu = fase_escolhida.iniciar(tela, teclas, jogador)
            if venceu:
                # fase 3 encerra o jogo
                if fase_escolhida.numero_fase == 3:
                    print("Você venceu!")
                    rodando = False
                else:
                    # Outras fases voltam ao lobby
                    fase_escolhida = None
                    jogador.x = X_JOGADOR
                    jogador.y = Y_JOGADOR

        # atualizar a tela e controlar FPS
        pygame.display.flip()
        clock.tick(FPS)
    # encerrar o pygame
    pygame.quit()

if __name__ == "__main__":
    main()