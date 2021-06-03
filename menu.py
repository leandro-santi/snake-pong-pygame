import pygame

import constants
import game
import instructions

size = (constants.WIDTH, constants.HEIGHT)
menu_screen = pygame.display.set_mode(size)


def main_menu():
    game.game()


def menu():
    while True:
        for click in pygame.event.get():
            if click.type == pygame.KEYDOWN:
                if click.key == pygame.K_SPACE:
                    main_menu()
                if click.key == pygame.K_i:
                    instructions.game_help()
                if click.key == pygame.K_ESCAPE:
                    pygame.quit()
            elif click.type == pygame.QUIT:
                pygame.quit()
            else:
                t_font = pygame.font.Font('assets/fonts/PressStart2P.ttf', 32)
                t_text = t_font.render('SNAKE+=PONG', True, constants.WHITE, constants.BLACK)
                t_text_rect = t_text.get_rect()
                t_text_rect.center = (300, 100)

                start_font = pygame.font.Font('assets/fonts/PressStart2P.ttf', 16)
                start_text = start_font.render('Press "SPACE" to start the game', True,
                                               constants.WHITE, constants.BLACK)
                start_text_rect = start_text.get_rect()
                start_text_rect.center = (300, 250)

                instruction_font = pygame.font.Font('assets/fonts/PressStart2P.ttf', 16)
                instruction_text = instruction_font.render('Press "i" to see the instructions', True,
                                                           constants.WHITE, constants.BLACK)
                instruction_text_rect = instruction_text.get_rect()
                instruction_text_rect.center = (300, 300)

                exit_font = pygame.font.Font('assets/fonts/PressStart2P.ttf', 16)
                exit_text = exit_font.render('Press "ESC" to exit', True, constants.WHITE, constants.BLACK)
                exit_text_rect = exit_text.get_rect()
                exit_text_rect.center = (300, 350)

                credits_font = pygame.font.Font('assets/fonts/PressStart2P.ttf', 12)
                credits_text = credits_font.render('© 2021 by: leosanti', True, constants.WHITE, constants.BLACK)
                credits2_text = credits_font.render('(Leandro Santiago da Silva)', True,
                                                    constants.WHITE, constants.BLACK)
                credits_text_rect = credits_text.get_rect()
                credits2_text_rect = credits2_text.get_rect()
                credits_text_rect.center = (300, 550)
                credits2_text_rect.center = (300, 570)

                menu_screen.fill(constants.BLACK)
                menu_screen.blit(t_text, t_text_rect)
                menu_screen.blit(start_text, start_text_rect)
                menu_screen.blit(instruction_text, instruction_text_rect)
                menu_screen.blit(exit_text, exit_text_rect)
                menu_screen.blit(credits_text, credits_text_rect)
                menu_screen.blit(credits2_text, credits2_text_rect)
                pygame.display.flip()
