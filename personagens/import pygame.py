import pygame
import sys


class Treinadora2(pygame.sprite.Sprite):
    PALETTE = {
        ".": None,
        "K": (24, 24, 24),
        "H": (44, 30, 26),
        "D": (68, 46, 40),
        "S": (140, 88, 56),
        "B": (104, 62, 38),
        "T": (42, 42, 48),
        "R": (224, 48, 48),
        "M": (112, 72, 48),
        "P": (32, 32, 38),
        "W": (248, 248, 248),
    }

    SPRITE_DATA = [
        ".KKK........KKK.",
        "KHHHK.KKKK.KHHHK",
        "KHDHHKHHHHKHHDHK",
        ".KKKHHHHHHHHKKK.",
        "..KHDDDDDDDDHK..",
        "..KHSSSSSSSSHK..",
        "..KSSKSSSSKSSK..",
        "..KSSKSSSSKSSK..",
        "...KBBBBBBBBK...",
        "....KKKKKKKK....",
        "..KKTTTTTTTTKK..",
        ".KTTMTTTRRTTTMK.",
        ".KSSTTTTRRTTSSK.",
        ".KSSTTTTTTTTSSK.",
        "..KKPPPPPPPPKK..",
        "..KPPPPPPPPPPK..",
        "..KKKKKKKKKKKK..",
        "...KSSSK.KSSSK..",
        "...KSSSK.KSSSK..",
        "...KBBBK.KBBBK..",
        "...KRRRK.KRRRK..",
        "..KWWRRK.KRRWWK.",
        "..KKKKKK.KKKKKK.",
        "................",
    ]

    def __init__(self, x, y, scale=4, speed=3):
        super().__init__()

        largura = 16
        altura = 24
        self.speed = speed

        imagem = pygame.Surface(
            (largura, altura),
            pygame.SRCALPHA
        )

        for linha_y, linha in enumerate(self.SPRITE_DATA):
            for coluna_x, letra in enumerate(linha):
                cor = self.PALETTE.get(letra)

                if cor is not None:
                    imagem.set_at((coluna_x, linha_y), cor)

        self.image_right = pygame.transform.scale(
            imagem,
            (largura * scale, altura * scale)
        )
        self.image_left = pygame.transform.flip(
            self.image_right,
            True,
            False
        )
        self.image = self.image_right
        self.rect = self.image.get_rect(center=(x, y))

    def update(self, keys=None, screen_w=None, screen_h=None):
        if keys is None:
            keys = pygame.key.get_pressed()

        if screen_w is None or screen_h is None:
            superficie = pygame.display.get_surface()

            if superficie is not None:
                screen_w, screen_h = superficie.get_size()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.image = self.image_left

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
            self.image = self.image_right

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed

        if screen_w and screen_h:
            limite = pygame.Rect(0, 0, screen_w, screen_h)
            self.rect.clamp_ip(limite)


def main():
    pygame.init()

    screen = pygame.display.set_mode((480, 320))
    pygame.display.set_caption("Treinadora 2")

    clock = pygame.time.Clock()
    treinadora = Treinadora2(240, 160)
    grupo = pygame.sprite.Group(treinadora)

    rodando = True

    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

        grupo.update()
        screen.fill((120, 200, 104))
        grupo.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()