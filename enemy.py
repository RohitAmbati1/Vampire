import pygame

import random

import math

import constants


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((10, 10))
        self.image.fill(constants.White)
        self.rect = self.image.get_rect()
        self.speed = 4
        self.health = 100

        side = random.choice(["t", "d", "l", "r"])

        if side == "t":
            y = random.randint(-30, -10)
            x = random.randint(-30, constants.screen_size[0] + 30)

        if side == "d":
            y = random.randint(constants.screen_size[1] + 10, constants.screen_size[1] + 30)
            x = random.randint(-30, constants.screen_size[0] + 30)

        if side == "l":
            y = random.randint(-30, constants.screen_size[1] + 30)
            x = random.randint(-30, -10)

        if side == "r":
            y = random.randint(-30, constants.screen_size[1] + 30)
            x = random.randint(constants.screen_size[0] + 10, constants.screen_size[0] + 30)

        self.rect.center = (x, y)

    def update(self, *args, **kwargs):
        player = kwargs["player"]

        # generates vector
        v = pygame.Vector2(
            player.centerx - self.rect.centerx,
            player.centery - self.rect.centery
        )

        if v.length() >= self.speed:
            v.normalize_ip()
            v.scale_to_length(self.speed)

        self.rect.center += v

    def decreaseHealth(self, damage):
        self.health -= damage

        if self.health <= 0:
            self.kill()
