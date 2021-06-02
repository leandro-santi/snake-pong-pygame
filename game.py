import pygame
import random

import constants
import menu


def game():
    pygame.init()

    game_screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
    pygame.display.set_caption('Snake+=Pong')

    # clock time para criar um tempo para o frame
    clock = pygame.time.Clock()

    # tamanho do bloco
    tamanho_objeto = 10
    tempo_objeto = 20


    def cobra(tamanho_objeto, matriz):
        for posx_y in matriz:
            pygame.draw.rect(game_screen, constants.GREEN, [posx_y[0], posx_y[1], tamanho_objeto, tamanho_objeto])


    def tela_msg(msg, cor):
        # desenha o texto em uma nova superficie
        tela_texto = constants.font.render(msg, True, cor)
        game_screen.blit(tela_texto, [25 , 300])


    def loop_jogo():
        sair_jogo = False
        gameOver = False

        # desempenho de colisao
        lado_x = constants.WIDTH / 2
        lado_y = constants.HEIGHT / 2

        # para a cobra ficar parada em (0) no inicio do jogo
        mudar_ladox = 0
        mudar_ladoy = 0

        matriz_cobra = []
        tamanho_cobra = 1

        # arredondamento de numeros aleatorios
        aleatorio_x = round(random.randrange(0, constants.HEIGHT - tamanho_objeto) / 10.0) * 10.0
        aleatorio_y = round(random.randrange(0, constants.WIDTH - tamanho_objeto) / 10.0) * 10.0

        # bloquea a tela e so sairá com as opções abaixo
        while not sair_jogo:

            while gameOver == True:
                game_screen.fill(constants.BLACK)
                tela_msg("Game over, C = continuar, Q = sair", constants.RED)

                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            menu.menu()
                            sair_jogo = True
                            gameOver = False
                        if event.key == pygame.K_c:
                            loop_jogo()

            # direções do blocos no teclado
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair_jogo = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        mudar_ladox = -tamanho_objeto
                        mudar_ladoy = 0
                    elif event.key == pygame.K_RIGHT:
                        mudar_ladox = tamanho_objeto
                        mudar_ladoy = 0
                    elif event.key == pygame.K_UP:
                        mudar_ladoy = -tamanho_objeto
                        mudar_ladox = 0
                    elif event.key == pygame.K_DOWN:
                        mudar_ladoy = tamanho_objeto
                        mudar_ladox = 0

            if lado_x >= constants.WIDTH or lado_x < 0 or lado_y >= constants.HEIGHT or lado_y < 0:
                gameOver = True

            lado_x += mudar_ladox
            lado_y += mudar_ladoy

            # cor da tela principal
            game_screen.fill(constants.BLACK)
            # cor do segundo objeto (comida)
            pygame.draw.rect(game_screen, constants.RED, [aleatorio_x, aleatorio_y, tamanho_objeto, tamanho_objeto])

            # matriz comida
            cabeca_cobra = []
            cabeca_cobra.append(lado_x)
            cabeca_cobra.append(lado_y)
            matriz_cobra.append(cabeca_cobra)

            # pega o tamanho da matriz (listaCobra2) define maior que o cumprimento
            if len(matriz_cobra) > tamanho_cobra:
                # remove o indice da matriz (0)
                del matriz_cobra[0]

            for seguimento_cobra in matriz_cobra[:-1]:
                if seguimento_cobra == cabeca_cobra:
                    gameOver = True

            cobra(tamanho_objeto, matriz_cobra)

            # atualiza o display
            pygame.display.update()

            # arredondamento de numeros aleatorios
            if lado_x == aleatorio_x and lado_y == aleatorio_y:
                aleatorio_x = round(random.randrange(0, constants.HEIGHT - tamanho_objeto) / 10.0) * 10.0
                aleatorio_y = round(random.randrange(0, constants.HEIGHT - tamanho_objeto) / 10.0) * 10.0
                tamanho_cobra += 1

            clock.tick(tempo_objeto)

        pygame.quit()
        quit()

    loop_jogo()
