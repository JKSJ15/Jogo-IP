import pygame
from classes.Jogador import Jogador
from classes.Letras import Letra
from classes.Porta import Porta
from uteis.colisao import checar_colisao
from constantes import LARGURA_TELA, ALTURA_TELA, FPS, VEL_JOGADOR, X_JOGADOR, Y_JOGADOR, COR_JOGADOR, VEL_LETRA 

def main():
    fase_atual = 0
    frases_coletadas = 0
    meta_frases = 25
    letras = [Letra(VEL_LETRA, "ABRACAO"), Letra(VEL_LETRA, "AMOR"), Letra(VEL_LETRA, "PAZ"), Letra(VEL_LETRA, "FELICIDADE"), Letra(VEL_LETRA, "SAUDE")]

    pygame.init()

    # tela e clock
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    clock = pygame.time.Clock()

    # inicializações
    jogador = Jogador(X_JOGADOR, Y_JOGADOR, VEL_JOGADOR)
    porta = Porta(LARGURA_TELA - 50, ALTURA_TELA - 50, 50, 50)

    # loop do jogo
    rodando = True
    while rodando:
        # teste de encerramento
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        # pegando teclas pressionadas
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_ESCAPE]:
            rodando = False
        
        # fase 0
        if fase_atual == 0:
            # desenhando tela
            tela.fill((0, 0, 0))
            jogador.desenhar(tela)
            porta.desenhar(tela)
            
            # Movimentação no mapa inicial
            jogador.mover(teclas)

            # Verificar colisão com a porta
            if checar_colisao(jogador, porta):
                fase_atual = 1

        # fase 1
        elif fase_atual == 1:
            # desenhando tela
            tela.fill((0, 0, 0))
            jogador.desenhar(tela)

            # Movimentação do jogador
            jogador.mover(teclas)

            # Movimentação das frases
            for letra in letras:
                letra.desenhar(tela)
                letra.mover()

                if checar_colisao(jogador, letra):
                    frases_coletadas += 1
                    letras.remove(letra)

            # Verificar se atingiu a meta
            if frases_coletadas >= meta_frases:
                fase_atual = 2

        # fase 2
        elif fase_atual == 2:
            # desenhando tela
            tela.fill((0, 0, 0))
            jogador.desenhar(tela)

            # Comportamento do terceiro cenário
            jogador.mover(teclas)

        # atualizando a tela e o clock
        pygame.display.flip()
        clock.tick(FPS)

    # sair
    pygame.quit()

if __name__ == "__main__":
    main()

    """# movendo objetos
            jogador.mover(teclas)
            letra.mover()
    
            # limpando e desenhado objetos na tela
            tela.fill((0, 0, 0))
            jogador.desenhar(tela)
            letra.desenhar(tela)
    
            # checando colisão
            if checar_colisao(jogador, letra):
                print("Colisão detectada!")
                jogador.x = -100000"""