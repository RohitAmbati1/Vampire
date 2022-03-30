import pygame
import math


class Aoe(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.radius = 50
        self.damage = 5
        self.rect = pygame.Rect(0, 0, self.radius * 2, self.radius * 2)
