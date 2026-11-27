import pygame
import sys

pygame.init()

# Configurações de tela e escala
SCALE = 4
SPRITE_W, SPRITE_H = 16, 24
SCREEN_W, SCREEN_H = 480, 320
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Treinador 16-bit - Estilo FireRed")
clock = pygame.time.Clock()

# Paleta 16-bit estilo GBA
PALETTE = {
    ".": None,              # Transparente
    "K": (24, 24, 24),      # Contorno escuro
    "H": (72, 48, 36),      # Cabelo castanho
    "D": (48, 32, 24),      # Sombra do cabelo
    "S": (248, 200, 152),   # Pele
    "T": (42, 42, 48),      # Camiseta preta
    "R": (224, 48, 48),     # Símbolo vermelho / Tênis
    "M": (112, 72, 48),     # Mochila / Alças
    "P": (36, 36, 44),      # Bermuda preta
    "W": (248, 248, 248),   # Detalhe branco do tênis
}

# Frente (16x24) - Cabelo castanho, camiseta preta com símbolo vermelho
DOWN_IDLE = [
    "....KKKKKK......",
    "...KHHHHHHK.....",
    "..KHHHHHHHHK....",
    "..KHHDDDDHHK....",
    "..KHDHHHHHDK....",
    "..KHSSSSSSHK....",
    "..KSSKSSKSSK....",
    "..KSSKSSKSSK....",
    "...KSSSSSSK.....",
    "....KKKKKK......",
    "..KKTTTTTTKK....",
    ".KTTTMTRRTTTK...",
    ".KSSTTTRRTTTSSK.",
    ".KSSTTTTTTTTSSK.",
    ".KKKTTTTTTKKK...",
    "...KPPPPPPK.....",
    "...KPPPPPPK.....",
    "...KPPKKPPK.....",
    "...KSSKKSSK.....",
    "...KSSKKSSK.....",
    "...KRRKKRRK.....",
    "..KWWRKKRWWK....",
    "..KKKKKKKKKK....",
    "................",
]

# Costas (16x24) - Cabelo castanho e mochila marrom
UP_IDLE = [
    "....KKKKKK......",
    "...KHHHHHHK.....",
    "..KHHHHHHHHK....",
    "..KHHHHHHHHK....",
    "..KHHDDDDHHK....",
    "..KHHHHHHHHK....",
    "..KHHDDDDHHK....",
    "...KHHHHHHK.....",
    "....KKKKKK......",
    "..KKMMMMMMKK....",
    ".KTTMMMMMMTTK...",
    ".KSSMMMMMMSSK...",
    ".KSSMMMMMMSSK...",
    ".KKKMMMMMMKKK...",
    "...KPPPPPPK.....",
    "...KPPPPPPK.....",
    "...KPPKKPPK.....",
    "...KSSKKSSK.....",
    "...KSSKKSSK.....",
    "...KRRKKRRK.....",
    "..KRRRKKRRRK....",
    "..KKKKKKKKKK....",
    "................",
    "................",
]

# Direita (16x24) - Perfil com mochila, camiseta preta e símbolo no peito
RIGHT_IDLE = [
    "....KKKKKK......",
    "...KHHHHHHK.....",
    "..KHHHHHHHHK....",
    "..KHHDDDDHHK....",
    "..KHHHHHHKKK....",
    "..KHHHSSSSK.....",
    "..KHHSSKSSK.....",
    "...KHSSSSSK.....",
    "....KSSSSK......",
    ".....KKKK.......",
    "..KKKTTTTKK.....",
    ".KMMMTTTTRSK....",
    ".KMMMTTTTRSK....",
    ".KMMMTTTTSSK....",
    "..KKKTTTTKK.....",
    "....KPPPPK......",
    "....KPPPPK......",
    "....KSSSSK......",
    "....KSSSSK......",
    "....KRRRRK......",
    "....KRWWWK......",
    "....KKKKKK......",
    "................",
    "................",
]

def build_surface(matrix, flip_x=False, step=0):
    surf = pygame.Surface((SPRITE_W, SPRITE_H), pygame.SRCALPHA)
    rows = list(matrix)

    # Alterna a altura das pernas para simular caminhada
    if step == 1:
        rows[18], rows[19] = rows[19], rows[18]
    elif step == 2:
        rows[19], rows[20] = rows[20], rows[19]

    for y, row in enumerate(rows):
        for x, ch in enumerate(row):
            color = PALETTE.get(ch)
            if color:
                surf.set_at((x, y), color)

    if flip_x:
        surf = pygame.transform.flip(surf, True, False)

    return pygame.transform.scale(surf, (SPRITE_W * SCALE, SPRITE_H * SCALE))

# Pré-renderiza os 4 frames de caminhada para cada direção
animations = {
    "down":  [build_surface(DOWN_IDLE, step=s) for s in (0, 1, 0, 2)],
    "up":    [build_surface(UP_IDLE, step=s) for s in (0, 1, 0, 2)],
    "right": [build_surface(RIGHT_IDLE, step=s) for s in (0, 1, 0, 2)],
    "left":  [build_surface(RIGHT_IDLE, flip_x=True, step=s) for s in (0, 1, 0, 2)],
}

player_x = SCREEN_W // 2 - (SPRITE_W * SCALE) // 2
player_y = SCREEN_H // 2 - (SPRITE_H * SCALE) // 2
direction = "down"
frame_idx = 0
anim_timer = 0
SPEED = 2.5

while True:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    moving = False

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_y += SPEED
        direction = "down"
        moving = True
    elif keys[pygame.K_UP] or keys[pygame.K_w]:
        player_y -= SPEED
        direction = "up"
        moving = True
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_x -= SPEED
        direction = "left"
        moving = True
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_x += SPEED
        direction = "right"
        moving = True

    if moving:
        anim_timer += dt
        if anim_timer >= 140:
            anim_timer = 0
            frame_idx = (frame_idx + 1) % 4
    else:
        frame_idx = 0

    screen.fill((120, 200, 104))
    screen.blit(animations[direction][frame_idx], (int(player_x), int(player_y)))
    pygame.display.flip()