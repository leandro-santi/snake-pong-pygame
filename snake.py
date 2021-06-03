import pygame

import game
import constants

pygame.init()


def snake(size, array):
    for position in array:
        pygame.draw.rect(game.game_screen, constants.GREEN, [position[0], position[1], size, size])
