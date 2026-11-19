import pygame

class Inimigo():
    def __init__(self, largura, altura, hp, dano):
        super().__init__();
        self.largura = largura
        self.altura = altura
        self.hp = hp
        self.dano = dano