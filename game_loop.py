import random

import pygame

from control import Control
from gui import Window
from snake import Snake
from food import Food

pygame.init()

window = Window()
snake = Snake()
food = Food()
control = Control(snake)


'''Главный цикл игры'''

while not control.game_over:
    control.control(snake)
    control.is_alive(window, snake)

    window.background_fill()

    food.render()
    snake.render()

    window.update()

    snake.eat_food(food)


pygame.quit()
quit()
