import pygame

class Audio:
    def __init__(self):
        self.permitida = pygame.mixer.Sound("sons/palavra_permitida.ogg")
        self.proibida = pygame.mixer.Sound("sons/proibidas.ogg")
        self.coracao = pygame.mixer.Sound("sons/coracao.ogg")
        self.raio = pygame.mixer.Sound("sons/raio.ogg")
        self.relogio = pygame.mixer.Sound("sons/relogio.ogg")
        self.sapato = pygame.mixer.Sound("sons/sapato.ogg")

        self.permitida.set_volume(0.5)
        self.proibida.set_volume(0.5)
        self.coracao.set_volume(0.5)
        self.raio.set_volume(0.5)
        self.relogio.set_volume(0.5)
        self.sapato.set_volume(0.5)