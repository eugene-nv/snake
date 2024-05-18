import pygame

from control import Control
from gui import Window, Message
from snake import Snake
from food import Food

pygame.init()

window = Window()
snake = Snake()
food = Food()
control = Control(snake, food, window)

'''Главный цикл игры'''


def game_loop():
    while not control.game_closed:

        while control.game_over:
            control.game_over_menu()

        control.control(snake)
        control.is_alive(window, snake)

        window.background_fill()

        food.render()
        snake.render()

        window.update()

        snake.eat_food(food)

    pygame.quit()
    quit()


game_loop()
