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

    window.background_fill()
    snake.create()
    window.update()

pygame.quit()
quit()
