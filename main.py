import pygame
from classes.Jogador import Jogador
from classes.Letras import Letra
from uteis.colisao import checar_colisao
from constantes import LARGURA_TELA, ALTURA_TELA, FPS, VEL_JOGADOR, X_JOGADOR, Y_JOGADOR, COR_JOGADOR, VEL_LETRA

def main():
    pygame.init()

    # tela e clock
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    clock = pygame.time.Clock()

    # inicializações
    jogador = Jogador(X_JOGADOR, Y_JOGADOR, VEL_JOGADOR)
    letra = Letra(VEL_LETRA)

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

        # movendo objetos
        jogador.mover(teclas)
        letra.mover()

        # limpando e desenhado objetos na tela
        tela.fill((0, 0, 0))
        jogador.desenhar(tela)
        letra.desenhar(tela)

        # checando colisão
        if checar_colisao(jogador, letra):
            print("Colisão detectada!")
            jogador.x = -100000

        # atualizando a tela e o clock
        pygame.display.flip()
        clock.tick(FPS)

    # sair
    pygame.quit()

if __name__ == "__main__":
    main()