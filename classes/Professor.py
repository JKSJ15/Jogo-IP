import pygame
from constantes import DIALOGO_FASE1, DIALOGO_FASE2, DIALOGO_FASE3
from uteis.pegarReacao import pegarReacao

class Professor(pegarReacao):
    # inicialização
    def __init__(self, x, y, nome):
        super().__init__()
        self.x = x
        self.y = y
        self.nome = nome

    # diálogos do professor
    def dialogar(self):
        if self.nome == "STEFAN":
            return DIALOGO_FASE1
        elif self.nome == "MARCIO":
            return DIALOGO_FASE2
        elif self.nome == "NAVIN":
            return DIALOGO_FASE3

    # desenhar o professor na tela
    def desenhar(self, tela):
        pygame.draw.circle(tela, (0, 0, 255), (self.x, self.y), 25)