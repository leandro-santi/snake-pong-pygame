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
head_snake = []
array_snake = []

sides = []


def game():
    pygame.init()

    # clock time para criar um tempo para o frame
    clock = pygame.time.Clock()

    """def screen_msg(msg, cor):
        # desenha o texto em uma nova superficie
        screen_text = constants.font.render(msg, True, cor)
        game_screen.blit(screen_text, [25, 300])
"""
    def loop_game():
        quit_game = False
        game_over = False

        global random_x
        global random_y
        global score
        global ball_speed
        global movement
        global head_snake
        global array_snake
        global sides

        up = 0
        down = 0
        right = 0
        left = 0

        score = 0

        collision_sound = pygame.mixer.Sound("assets/sounds/bounce.wav")
        eating_sound = pygame.mixer.Sound("assets/sounds/eating.wav")

        ball.ball_x = 300
        ball.ball_y = 300

        ball_speed = 3
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
                # game_screen.fill(constants.BG_COLOR)
                background = pygame.image.load("assets/images/sand_ground.png")
                game_screen.blit(background, (0, 0))

                screen_bg = pygame.image.load("assets/images/snake_egg_broken.png")
                game_over_font = pygame.font.Font('assets/fonts/PressStart2P.ttf', 32)
                game_over_text = game_over_font.render('GAME OVER!', True, constants.BLACK)
                game_over_text_rect = game_over_text.get_rect()
                game_over_text_rect.center = (300, 100)
                game_screen.blit(game_over_text, game_over_text_rect)

                game_over_font1 = pygame.font.Font('assets/fonts/PressStart2P.ttf', 16)
                game_over_text1 = game_over_font1.render('Press "Q" to back to Menu', True, constants.BLACK)
                game_over_text1_rect = game_over_text1.get_rect()
                game_over_text1_rect.center = (300, 500)
                game_screen.blit(game_over_text1, game_over_text1_rect)

                continue_font1 = pygame.font.Font('assets/fonts/PressStart2P.ttf', 16)
                continue_text1 = continue_font1.render('Press "C" to continue', True, constants.BLACK)
                continue_text1_rect = continue_text1.get_rect()
                continue_text1_rect.center = (300, 550)
                game_screen.blit(continue_text1, continue_text1_rect)

                score_font1 = pygame.font.Font('assets/fonts/PressStart2P.ttf', 16)
                score_text1 = score_font1.render('Score: %02d' % score, True, constants.BLACK)
                score_text1_rect = score_text1.get_rect()
                score_text1_rect.center = (300, 175)
                game_screen.blit(score_text1, score_text1_rect)

                game_screen.blit(screen_bg, (150, 150))
                # screen_msg("Game over, C = continuar, Q = sair", constants.WHITE)

                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            menu.menu()
                            quit_game = True
                            game_over = False
                            ball_speed = 3
                            ball.ball_dx = 3
                            ball.ball_dy = 3
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
                            size_snake += 20
                            game_start = False
                        change_side_y = 0
                        movement = True
                        up = 0
                        down = 0
                        right = 0
                        left = 1
                        snake.vector = (-1, 0)
                        # sides.append(-1)
                        # print(sides[len(sides) - 1])
                        # print(snake.vector)
                    elif event.key == pygame.K_RIGHT:
                        change_side_x = constants.block_size
                        if game_start:
                            size_snake += 20
                            game_start = False
                        change_side_y = 0
                        movement = True
                        up = 0
                        down = 0
                        right = 1
                        left = 0
                        snake.vector = (1, 0)
                        # sides.append(1)
                        # print(sides[len(sides) - 1])
                        # print(snake.vector)
                    elif event.key == pygame.K_UP:
                        change_side_y = -constants.block_size
                        if game_start:
                            size_snake += 20
                            game_start = False
                        change_side_x = 0
                        movement = True
                        up = 1
                        down = 0
                        right = 0
                        left = 0
                        snake.vector = (0, 1)
                        # sides.append(2)
                        # print(sides[len(sides) - 1])
                        # print(snake.vector)
                    elif event.key == pygame.K_DOWN:
                        change_side_y = constants.block_size
                        if game_start:
                            size_snake += 20
                            game_start = False
                        change_side_x = 0
                        movement = True
                        up = 0
                        down = 1
                        right = 0
                        left = 0
                        snake.vector = (0, -1)
                        # sides.append(-2)
                        # print(sides[len(sides) - 1])
                        # print(snake.vector)

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
            background = pygame.image.load("assets/images/sand_ground.png")
            game_screen.blit(background, (0, 0))
            # game_screen.fill(constants.BG_COLOR)

            # cor do segundo objeto (comida)
            # pygame.draw.rect(game_screen, constants.RED, [random_x, random_y,
            # constants.block_size, constants.block_size])
            apple = pygame.image.load("assets/images/golden_apple.png")
            game_screen.blit(apple, (random_x, random_y))

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
            # balls = pygame.Rect(ball.ball_x, ball.ball_y, 10, 10)
            balls = pygame.image.load("assets/images/snake_egg.png")
            # pygame.draw.rect(game_screen, constants.WHITE, balls)
            game_screen.blit(balls, (ball.ball_x, ball.ball_y))
            # pygame.display.flip()

            #  colisão da bolinha
            if ball.ball_x >= constants.WIDTH or ball.ball_x < 0 or ball.ball_y >= constants.HEIGHT or ball.ball_y < 0:
                game_over = True
            # print(array_snake[0][0] == ball.ball_x)
            # print(array_snake[0][1] == ball.ball_y)
            # colisão da bolinha com a cobra
            for rub in array_snake[:-1]:
                if ball.ball_x - 10 <= rub[0] <= ball.ball_x + 10 and\
                        ball.ball_y - 10 <= rub[1] <= ball.ball_y + 10 and movement:
                    # aux = random.randint(0, 1)
                    if left == 1:
                        ball.ball_dx = abs(ball.ball_dx) * -1
                        ball.ball_dy *= -1
                    elif right == 1:
                        ball.ball_dx = abs(ball.ball_dx) * 1
                        ball.ball_dy *= -1
                    elif up == 1:
                        ball.ball_dx *= -1
                        ball.ball_dy = abs(ball.ball_dy) * -1
                    elif down == 1:
                        ball.ball_dx *= -1
                        ball.ball_dy = abs(ball.ball_dy) * 1
                    # print(rub[0], ball.ball_x)
                    # print(rub[1], ball.ball_y)

                    # print(constants.ang[aux])
                    # print(ball_speed)
                    collision_sound.play()
                    movement = False
                    # ball.ball_dx *= constants.ang[aux]
                    # ball.ball_dy *= -1

            # Texto de score
            score_game_font = pygame.font.Font('assets/fonts/PressStart2P.ttf', 16)
            score_game_text = score_game_font.render('Score: %02d' % score, True, constants.BLACK)
            score_game_text_rect = score_game_text.get_rect()
            score_game_text_rect.center = (300, 12)
            game_screen.blit(score_game_text, score_game_text_rect)

            # atualiza o display
            pygame.display.update()

            # arredondamento de numeros aleatorios / crescimento da snake
            if random_x - 10 <= side_x <= random_x + 10 and random_y - 10 <= side_y <= random_y + 10:
                random_x = round(random.randrange(50, (constants.HEIGHT - 50) - constants.block_size) / 10.0) * 10.0
                random_y = round(random.randrange(50, (constants.HEIGHT - 50) - constants.block_size) / 10.0) * 10.0
                if size_snake > 3:
                    size_snake -= 1
                    del array_snake[0]
                    # print(len(array_snake))
                score += 1
                eating_sound.play()

            clock.tick(constants.block_time)

        pygame.quit()
        quit()

    loop_game()
