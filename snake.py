import pygame

import game
import constants

pygame.init()

vector = (0, 0)

head_up = pygame.image.load('assets/images/head_up.png')
head_down = pygame.image.load('assets/images/head_down.png')
head_right = pygame.image.load('assets/images/head_right.png')
head_left = pygame.image.load('assets/images/head_left.png')

right = True
left = False
up = False
down = True

flag = True


def snake(size, array):
    global right
    global left
    global up
    global down
    global flag

    # draw snake
    for index, position in enumerate(array):
        # pygame.draw.rect(game.game_screen, constants.GREEN, [position[0], position[1], size, size])
        # x_pos = int(position[0] * size)
        # y_pos = int(position[1] * size)
        block_rect = pygame.Rect([position[0], position[1], size, size])

        if index == len(array) - 1:
            if vector == (1, 0):
                game.game_screen.blit(head_right, block_rect)
            elif vector == (-1, 0):
                game.game_screen.blit(head_left, block_rect)
            elif vector == (0, 1):
                game.game_screen.blit(head_up, block_rect)
            elif vector == (0, -1):
                game.game_screen.blit(head_down, block_rect)

        else:
            pygame.draw.rect(game.game_screen, constants.SNAKE_COLOR, [position[0], position[1], size, size])
