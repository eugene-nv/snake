import pygame
from gui import Window
from snake import Snake

pygame.init()

window = Window()
snake = Snake(window)

'''Главный цикл игры'''

game_over = False
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.change_x = -10
                snake.change_y = 0
            elif event.key == pygame.K_RIGHT:
                snake.change_x = 10
                snake.change_y = 0
            elif event.key == pygame.K_UP:
                snake.change_y = -10
                snake.change_x = 0
            elif event.key == pygame.K_DOWN:
                snake.change_y = 10
                snake.change_x = 0

    snake.x += snake.change_x
    snake.y += snake.change_y

    window.background_fill()
    snake.render()
    window.update()

pygame.quit()
quit()
