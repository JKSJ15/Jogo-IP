import pygame

from cenarios.fase1 import (
    canvas as canvas_fase1,
    render_room as render_room_fase1
)
from cenarios.fase2 import (
    canvas as canvas_fase2,
    render_room as render_room_fase2
)
from cenarios.fase3 import (
    canvas as canvas_fase3,
    render_room as render_room_fase3
)

class Cenario:
    def _desenhar(self, tela, canvas, render_room):
        render_room()
        fator = min(
            tela.get_width() / canvas.get_width(),
            tela.get_height() / canvas.get_height()
        )

        largura = int(canvas.get_width() * fator)
        altura = int(canvas.get_height() * fator)

        scaled_surface = pygame.transform.scale(
            canvas,
            (largura, altura)
        )

        x = (tela.get_width() - largura) // 2
        y = (tela.get_height() - altura) // 2

        tela.blit(scaled_surface, (x, y))

    def desenharFase1(self, tela):
        self._desenhar(tela, canvas_fase1, render_room_fase1)

    def desenharFase2(self, tela):
        self._desenhar(tela, canvas_fase2, render_room_fase2)

    def desenharFase3(self, tela):
        self._desenhar(tela, canvas_fase3, render_room_fase3)