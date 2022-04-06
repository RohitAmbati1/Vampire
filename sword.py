import pygame

import constants


class Sword(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        image = pygame.Surface((75, 75)).convert_alpha()
        image.fill(constants.Transparent)
        pygame.draw.circle(image, constants.Yellow, image.get_rect().center, 37.5)
        self.image = pygame.Surface((37.5, 75)).convert_alpha()
        self.image.fill(constants.Transparent)
        self.image.blit(image.subsurface(pygame.Rect(37.5, 0, 37.5, 75)), (0, 0))

        self.rect = self.image.get_rect()
