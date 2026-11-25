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

    # Fases
    fase1 = Fase(1)
    fase2 = Fase(2)
    fase3 = Fase(3)

    # variáveis de controle
    fase_atual = fase1
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

        # EXECUÇÃO DA FASE
        venceu = fase_atual.iniciar(tela, teclas, jogador, eventos)
        if venceu:
            if fase_atual.numero_fase == 3:
                print("Você venceu!")
                rodando = False
            else:
                if fase_atual.numero_fase == 1:
                    fase_atual = fase2
                elif fase_atual.numero_fase == 2:
                    fase_atual = fase3

                fase_atual.reiniciar()

                jogador.x = X_JOGADOR
                jogador.y = Y_JOGADOR
                
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()