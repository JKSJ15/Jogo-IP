import pygame
from cenarios.fase1 import canvas, PALETTE, render_room

class Cenario:
    def desenharFase1(self, tela):
        render_room()
        scaled_surface = pygame.transform.scale(canvas, tela.get_size())
        tela.blit(scaled_surface, (0, 0))

    def desenharFase2(self, tela):
        # Implementar a lógica para desenhar o cenário da Fase 2
        pass

    def desenharFase3(self, tela):
        # Implementar a lógica para desenhar o cenário da fase 3
        pass