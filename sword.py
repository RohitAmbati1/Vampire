import pygame

import constants


class Sword(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((75, 75))
        self.image.fill(constants.Blue)
        self.rect = pygame.Rect(400, 250, 1, 1)
