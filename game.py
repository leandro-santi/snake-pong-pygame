import pygame
import random

import constants
import menu
import snake
import ball

game_screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
pygame.display.set_caption('Snake+=Pong')

random_x = 0
random_y = 0
score = 0
ball_speed = 0
movement = False


def game():
    pygame.init()

    # clock time para criar um tempo para o frame
    clock = pygame.time.Clock()

    def screen_msg(msg, cor):
        # desenha o texto em uma nova superficie
        screen_text = constants.font.render(msg, True, cor)
        game_screen.blit(screen_text, [25, 300])

    def loop_game():
        quit_game = False
        game_over = False

        global random_x
        global random_y
        global score
        global ball_speed
        global movement

        ball.ball_x = 300
        ball.ball_y = 300

        ball_speed = 2
        movement = False

        # desempenho de colisao
        side_x = constants.WIDTH / 2
        side_y = constants.HEIGHT / 2

        # para a snake ficar parada em (0) no inicio do jogo
        change_side_x = 0
        change_side_y = 0

        array_snake = []
        size_snake = 1

        game_start = True

        # arredondamento de numeros aleatorios
        random_x = round(random.randrange(0, constants.HEIGHT - constants.block_size) / 10.0) * 10.0
        random_y = round(random.randrange(0, constants.WIDTH - constants.block_size) / 10.0) * 10.0

        # bloquea a tela e so sairá com as opções abaixo
        while not quit_game:

            while game_over:
                game_screen.fill(constants.BLACK)
                screen_msg("Game over, C = continuar, Q = sair", constants.WHITE)

                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            menu.menu()
                            quit_game = True
                            game_over = False
                            ball_speed = 1
                            ball.ball_dx = 1
                            ball.ball_dy = 1
                        if event.key == pygame.K_c:
                            loop_game()

            # direções do blocos no teclado
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        change_side_x = -constants.block_size
                        if game_start:
                            size_snake += 15
                            game_start = False
                        change_side_y = 0
                        movement = True
                    elif event.key == pygame.K_RIGHT:
                        change_side_x = constants.block_size
                        if game_start:
                            size_snake += 15
                            game_start = False
                        change_side_y = 0
                        movement = True
                    elif event.key == pygame.K_UP:
                        change_side_y = -constants.block_size
                        if game_start:
                            size_snake += 15
                            game_start = False
                        change_side_x = 0
                        movement = True
                    elif event.key == pygame.K_DOWN:
                        change_side_y = constants.block_size
                        if game_start:
                            size_snake += 15
                            game_start = False
                        change_side_x = 0
                        movement = True

            # Snake atravessando as paredes
            if side_x >= constants.WIDTH or side_x < 0 or side_y >= constants.HEIGHT or side_y < 0:
                # game_over = True
                if side_x > constants.WIDTH:
                    side_x = 0
                elif side_x < 0:
                    side_x = constants.WIDTH
                elif side_y > constants.HEIGHT:
                    side_y = 0
                elif side_y < 0:
                    side_y = constants.HEIGHT

            side_x += change_side_x
            side_y += change_side_y

            # cor da tela principal
            game_screen.fill(constants.BLACK)

            # cor do segundo objeto (comida)
            pygame.draw.rect(game_screen, constants.RED, [random_x, random_y,
                                                          constants.block_size, constants.block_size])

            # matriz comida
            head_snake = [side_x, side_y]
            array_snake.append(head_snake)

            # pega o tamanho da matriz (listaCobra2) define maior que o cumprimento
            if len(array_snake) > size_snake:
                # remove o indice da matriz (0)
                del array_snake[0]

            for length_snake in array_snake[:-1]:
                if length_snake == head_snake:
                    game_over = True

            snake.snake(constants.block_size, array_snake)
            # ball.draw_ball()

            # movimento da bolinha
            ball.ball_x += ball.ball_dx
            ball.ball_y += ball.ball_dy
            balls = pygame.Rect(ball.ball_x, ball.ball_y, 10, 10)
            pygame.draw.rect(game_screen, constants.WHITE, balls)
            # game_screen.blit(ball.ball, (ball.ball_x, ball.ball_y))
            # pygame.display.flip()

            #  colisão da bolinha
            if ball.ball_x >= constants.WIDTH or ball.ball_x < 0 or ball.ball_y >= constants.HEIGHT or ball.ball_y < 0:
                game_over = True
            # print(array_snake[0][0] == ball.ball_x)
            # print(array_snake[0][1] == ball.ball_y)
            # colisão da bolinha com a cobra
            for rub in array_snake[:-1]:
                if ball.ball_x - 10 <= rub[0] <= ball.ball_x + 10 and ball.ball_y - 10 <= rub[1] <= ball.ball_y + 10 and movement == True:
                    print(rub[0], ball.ball_x)
                    print(rub[1], ball.ball_y)
                    # aux = random.randint(0, 1)
                    # print(constants.ang[aux])
                    # print(ball_speed)
                    movement = False
                    ball.ball_dx *= -1
                    ball.ball_dy *= -1

            # atualiza o display
            pygame.display.update()

            # arredondamento de numeros aleatorios / crescimento da snake
            if side_x == random_x and side_y == random_y:
                random_x = round(random.randrange(0, constants.HEIGHT - constants.block_size) / 10.0) * 10.0
                random_y = round(random.randrange(0, constants.HEIGHT - constants.block_size) / 10.0) * 10.0
                if size_snake > 3:
                    size_snake -= 1
                    del array_snake[0]
                    # print(len(array_snake))

            clock.tick(constants.block_time)

        pygame.quit()
        quit()

    loop_game()
