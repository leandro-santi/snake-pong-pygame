import pygame

import constants
import menu

size = (constants.WIDTH, constants.HEIGHT)
help_screen = pygame.display.set_mode(size)


def game_help():

    while True:
        for click in pygame.event.get():
            if click.type == pygame.KEYDOWN:
                if click.key == pygame.K_i:
                    menu.menu()
                if click.key == pygame.K_ESCAPE:
                    pygame.quit()
            elif click.type == pygame.QUIT:
                pygame.quit()
            else:
                help_font = pygame.font.Font('assets/fonts/PressStart2P.ttf', 16)
                help2_font = pygame.font.Font('assets/fonts/PressStart2P.ttf', 10)

                help1_text = help_font.render('Objective:', True,
                                              constants.WHITE, constants.BLACK)
                help1_text_rect = help1_text.get_rect()
                help1_text_rect.center = (300, 100)

                help2_text = help2_font.render('Eat apples without leave the snake´s egg hit the walls.', True,
                                               constants.WHITE, constants.BLACK)
                help2_text_rect = help2_text.get_rect()
                help2_text_rect.center = (300, 150)

                help3_text = help2_font.render('Beat on the snake´s egg to change its direction.', True,
                                               constants.WHITE, constants.BLACK)
                help3_text_rect = help3_text.get_rect()
                help3_text_rect.center = (300, 200)

                help4_text = help_font.render('Mechanics:', True, constants.WHITE, constants.BLACK)
                help4_text_rect = help4_text.get_rect()
                help4_text_rect.center = (300, 300)

                help5_text = help2_font.render('UP, DOWN, LEFT, RIGHT to move the snake.', True, constants.WHITE,
                                               constants.BLACK)
                help5_text_rect = help5_text.get_rect()
                help5_text_rect.center = (300, 350)

                help6_text = help2_font.render('Eat apples will make the snake decrease.', True,
                                               constants.WHITE, constants.BLACK)
                help6_text_rect = help6_text.get_rect()
                help6_text_rect.center = (300, 400)

                help7_text = help2_font.render('SAVE THE SNAKE´S BABY!', True,
                                               constants.WHITE, constants.BLACK)
                help7_text_rect = help7_text.get_rect()
                help7_text_rect.center = (300, 450)

                exit_help_text = help2_font.render('Press "i" to back to menu.', True,
                                                   constants.WHITE, constants.BLACK)
                exit_help_text_rect = exit_help_text.get_rect()
                exit_help_text_rect.center = (300, 550)

                help_screen.fill(constants.BLACK)
                help_screen.blit(help1_text, help1_text_rect)
                help_screen.blit(help2_text, help2_text_rect)
                help_screen.blit(help3_text, help3_text_rect)
                help_screen.blit(help4_text, help4_text_rect)
                help_screen.blit(help5_text, help5_text_rect)
                help_screen.blit(help6_text, help6_text_rect)
                help_screen.blit(help7_text, help7_text_rect)
                help_screen.blit(exit_help_text, exit_help_text_rect)
                pygame.display.flip()
