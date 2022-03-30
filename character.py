import pygame

import constants

import utilities

import aoe


class Character(pygame.sprite.Sprite):
    def __init__(self, sword):
        super().__init__()
        self.image = pygame.Surface((15, 15))
        self.image.fill(constants.Red)
        self.rect = self.image.get_rect()
        self.rect.center = (constants.screen_size[0] / 2, constants.screen_size[1] / 2)
        self.speed = 5
        self.aoe = aoe.Aoe()
        self.sword = sword

    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print("swing")

    def update(self, *args, **kwargs):
        keymap = pygame.key.get_pressed()
        if keymap[pygame.K_UP]:
            self.rect.y -= self.speed

        if keymap[pygame.K_DOWN]:
            self.rect.y += self.speed

        if keymap[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if keymap[pygame.K_RIGHT]:
            self.rect.x += self.speed

        if self.rect.right > constants.screen_size[0]:
            self.rect.right = constants.screen_size[0]

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > constants.screen_size[1]:
            self.rect.bottom = constants.screen_size[1]

        enemies = kwargs["enemies"]

        for e in enemies:
            if utilities.inrange(
                    (self.rect.centerx, self.rect.centery),
                    (e.rect.centerx, e.rect.centery),
                    self.aoe.radius
            ):
                e.decreaseHealth(5)
