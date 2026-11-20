import pygame

def checar_colisao(objeto1, objeto2):
    obg1 = pygame.Rect(objeto1.pegar_reacao())
    obg2 = pygame.Rect(objeto2.pegar_reacao())
    return obg1.colliderect(obg2)