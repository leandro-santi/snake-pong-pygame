import pygame

pygame.font.init()

# define cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 155, 0)
SNAKE_COLOR = (245, 141, 67)
BG_COLOR = (244, 236, 164)

WIDTH = 600
HEIGHT = 600

font = pygame.font.Font("assets/fonts/PressStart2P.ttf", 16)

# block constants
block_size = 10
block_time = 20

# random angle
ang = [1, -1]
