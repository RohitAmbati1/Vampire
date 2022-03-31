import pygame

import constants


class Sword(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        image = pygame.Surface((75, 75))
        image.fill(constants.Blue)
        self.image = pygame.Surface((37.5,75))
        self.image.blit(image,(0,0))  # todo: check which part of the image to blit

        self.rect = self.image.get_rect()


