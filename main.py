import pygame
from classes.Jogador import Jogador
from classes.Porta import Porta
from classes.Fase import Fase
from uteis.colisao import checar_colisao
from constantes import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    VEL_JOGADOR,
    X_JOGADOR,
    Y_JOGADOR
)

def main():
    # Inicializa e configura o pygame
    pygame.init()
    tela = pygame.display.set_mode(
        (LARGURA_TELA, ALTURA_TELA)
    )
    pygame.display.set_caption("Vamos CinBora")
    clock = pygame.time.Clock()

    # Instanciando objetos do jogo
    # Jogador
    jogador = Jogador(
        X_JOGADOR,
        Y_JOGADOR,
        VEL_JOGADOR
    )
    
    # Portas do menu
    porta1 = Porta(100, 200, 100, 150)
    porta2 = Porta(350, 200, 100, 150)
    porta3 = Porta(600, 200, 100, 150)

    # Fases
    fase1 = Fase(1)
    fase2 = Fase(2)
    fase3 = Fase(3)

    # variáveis de controle
    fase_escolhida = None
    rodando = True

    # Loop principal
    while rodando:
        eventos = pygame.event.get()

        # Verificar saída do jogo
        for evento in eventos:
            if evento.type == pygame.QUIT:
                rodando = False

        # Capturar teclas pressionadas
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_ESCAPE]:
            rodando = False
        tela.fill((30, 30, 30))

        # MENU DE SELEÇÃO
        if fase_escolhida is None:
            porta1.desenhar(tela)
            porta2.desenhar(tela)
            porta3.desenhar(tela)

            jogador.mover(teclas)
            jogador.desenhar(tela)

            # Escolha da fase por colisão
            if checar_colisao(jogador, porta1):
                fase_escolhida = fase1

            elif checar_colisao(jogador, porta2):
                fase_escolhida = fase2

            elif checar_colisao(jogador, porta3):
                fase_escolhida = fase3

            # Reiniciar posição do jogador
            if fase_escolhida is not None:
                jogador.x = X_JOGADOR
                jogador.y = Y_JOGADOR
                fase_escolhida.reiniciar()

        # EXECUÇÃO DA FASE
        else:
            venceu = fase_escolhida.iniciar(tela, teclas, jogador, eventos)
            if venceu:
                if fase_escolhida.numero_fase == 3:
                    print("Você venceu!")
                    rodando = False
                else:
                    fase_escolhida = None
                    jogador.x = X_JOGADOR
                    jogador.y = Y_JOGADOR

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()