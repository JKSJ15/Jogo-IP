import pygame


class Personagem:

    def __init__(self, nome="Alex", sprite_path="personagem.png"):
        # Identidade e aparência (estilo Pokémon FireRed)
        self.nome = nome
        self.idade = 30
        self.classe = "Treinador Veterano"
        self.aparencia = {
            "cabelo": "cacheado castanho-escuro",
            "bone": False,
            "barba": False,
            "camisa": "polo preta",
            "calca": "jeans azul",
            "calcado": "sapatos marrons",
        }

        # Atributos de jogo
        self.dinheiro = 3000
        self.insignias = []
        self.equipe = []  # Máximo de 6 Pokémon
        self.mochila = {"Poké Bola": 5, "Super Poção": 3}

        # Carregamento do sprite (escala padrão GBA 32x32)
        self.sprite = self._carregar_sprite(sprite_path)

    def _carregar_sprite(self, caminho):
        try:
            imagem = pygame.image.load(caminho).convert_alpha()
            return pygame.transform.scale(imagem, (32, 32))
        except (pygame.error, FileNotFoundError):
            # Placeholder com a cor da polo preta caso o arquivo não exista ainda
            placeholder = pygame.Surface((32, 32))
            placeholder.fill((30, 30, 30))
            return placeholder

    def adicionar_pokemon(self, pokemon):
        if len(self.equipe) < 6:
            self.equipe.append(pokemon)

    def desenhar(self, tela, x, y):
        tela.blit(self.sprite, (x, y))


# Criando o personagem
personagem = Personagem(nome="Alex", sprite_path="personagem.png")
personagem.adicionar_pokemon("Growlithe")