import pygame

pygame.init()

import character

import constants

import enemy

import sword

screen = pygame.display.set_mode(constants.screen_size)
pygame.display.set_caption("Vampire")

clock = pygame.time.Clock()

def main():
    contenders = pygame.sprite.Group()

    enemies = pygame.sprite.Group()

    attacks = pygame.sprite.Group()

    for i in range(20):
        enemies.add(enemy.Enemy())

    blade = sword.Sword()

    player = character.Character(blade)

    contenders.add(player)

    attacks.add(blade)

    done = False

    while not done:

        # 1 handle all events

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            player.handleEvent(event)

        # 2 update things (any type of calculation)

        contenders.update(enemies=enemies)

        enemies.update(player=player.rect)

        # 3 drawing stuff on screen and showing newest frame

        screen.fill(constants.Black)

        enemies.draw(screen)

        contenders.draw(screen)

        attacks.draw(screen)

        pygame.display.flip()

        clock.tick(60)


if __name__ == "__main__":
    main()
