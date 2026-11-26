import pygame
from classes.Jogador import Jogador
from classes.Porta import Porta
from classes.Fase import Fase
from classes.TelaFinal import TelaFinal
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
    estado_jogo = "jogando"
    tela_final = TelaFinal("vitoria")

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
        if estado_jogo == "jogando":
            venceu = fase_atual.iniciar(tela, teclas, jogador, eventos)

            if venceu:
                if fase_atual.numero_fase == 3:
                    # passou pela última fase: tela de vitória
                    estado_jogo = "fim"
                    tela_final = TelaFinal("vitoria", "Você passou pelas 3 fases!")
                else:
                    if fase_atual.numero_fase == 1:
                        fase_atual = fase2
                    elif fase_atual.numero_fase == 2:
                        fase_atual = fase3

                    fase_atual.reiniciar()

                    jogador.x = X_JOGADOR
                    jogador.y = Y_JOGADOR

            elif fase_atual.estado == "morte":
                # sem vidas e sem reinícios: tela de derrota
                estado_jogo = "fim"
                tela_final = TelaFinal(
                    "derrota",
                    f"Você não passou da fase {fase_atual.numero_fase} - sala {fase_atual.nome_sala}"
                )

        # TELA FINAL (vitória ou derrota)
        else:
            acao = tela_final.atualizar(tela, eventos)

            if acao == "reiniciar":
                # começa tudo do zero
                fase1 = Fase(1)
                fase2 = Fase(2)
                fase3 = Fase(3)
                fase_atual = fase1
                jogador.x = X_JOGADOR
                jogador.y = Y_JOGADOR
                estado_jogo = "jogando"

            elif acao == "sair":
                rodando = False
                
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()