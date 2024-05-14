import pygame

from control import Control
from gui import Window
from snake import Snake

pygame.init()

window = Window()
snake = Snake(window)
control = Control(snake)

'''Главный цикл игры'''

while not control.game_over:
    control.control(snake)
    control.is_alive(window)

    window.background_fill()
    snake.render()
    window.update()

pygame.quit()
quit()
