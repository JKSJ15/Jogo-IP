import pygame

def checar_colisao(objeto1, objeto2):
    rect_a = pygame.Rect(objeto1.get_rect())
    rect_b = pygame.Rect(objeto2.get_rect())
    return rect_a.colliderect(rect_b)