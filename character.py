import pygame

import constants

import utilities

import aoe

import math


class Character(pygame.sprite.Sprite):
    def __init__(self, sword):
        super().__init__()
        self.image = pygame.Surface((15, 15)).convert_alpha()
        self.image.fill(constants.Red)
        self.baseimage = self.image.copy()
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
        mousepos = pygame.mouse.get_pos()
        if keymap[pygame.K_w]:
            self.rect.y -= self.speed

        if keymap[pygame.K_s]:
            self.rect.y += self.speed

        if keymap[pygame.K_a]:
            self.rect.x -= self.speed

        if keymap[pygame.K_d]:
            self.rect.x += self.speed

        if self.rect.right > constants.screen_size[0]:
            self.rect.right = constants.screen_size[0]

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > constants.screen_size[1]:
            self.rect.bottom = constants.screen_size[1]

        # aimdirection = pygame.math.Vector2(self.rect.center).angle_to(pygame.math.Vector2(mousepos))
        aimdirection = pygame.math.Vector2(mousepos) - pygame.math.Vector2(self.rect.center)
        aimangle = math.degrees(math.atan2(aimdirection.y, aimdirection.x))
        #print(aimangle)
        self.image = pygame.transform.rotate(self.baseimage, -aimangle)

        enemies = kwargs["enemies"]

        for e in enemies:
            if utilities.inrange(
                    (self.rect.centerx, self.rect.centery),
                    (e.rect.centerx, e.rect.centery),
                    self.aoe.radius
            ):
                e.decreaseHealth(5)

        self.sword.rect.midleft = self.rect.center
