import pygame

from cenarios.fase1 import (
    canvas as canvas_fase1,
    render_room as render_room_fase1,
    DOOR_RECT as DOOR_FASE1,
)
from cenarios.fase2 import (
    canvas as canvas_fase2,
    render_room as render_room_fase2,
    DOOR_RECT as DOOR_FASE2,
)
from cenarios.fase3 import (
    canvas as canvas_fase3,
    render_room as render_room_fase3,
    DOOR_RECT as DOOR_FASE3,
)

# Quanto a área de colisão da porta "sai" do desenho (em pixels da TELA),
# para o jogador conseguir encostar mesmo a porta estando na parede.
MARGEM_PORTA = 30

class Cenario:
    def __init__(self):
        self.porta_rect = pygame.Rect(0, 0, 0, 0)

    def _desenhar(self, tela, canvas, render_room, door_rect):
        render_room()

        tela_w, tela_h = tela.get_size()

        # Estica o canvas para ocupar a janela inteira
        superficie = pygame.transform.scale(canvas, (tela_w, tela_h))
        tela.blit(superficie, (0, 0))

        # Converte a porta (coordenadas do canvas) para coordenadas da tela
        sx = tela_w / canvas.get_width()
        sy = tela_h / canvas.get_height()
        self.porta_rect = pygame.Rect(
            int(door_rect.x * sx),
            int(door_rect.y * sy),
            int(door_rect.w * sx),
            int(door_rect.h * sy),
        ).inflate(MARGEM_PORTA, MARGEM_PORTA)

    def desenhar(self, numero_fase, tela):
        if numero_fase == 1:
            self._desenhar(tela, canvas_fase1, render_room_fase1, DOOR_FASE1)
        elif numero_fase == 2:
            self._desenhar(tela, canvas_fase2, render_room_fase2, DOOR_FASE2)
        else:
            self._desenhar(tela, canvas_fase3, render_room_fase3, DOOR_FASE3)