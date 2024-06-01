import pygame

from system.control import Control
from system.gui import Window, Message
from system.snake import Snake
from system.food import Food

pygame.init()

window = Window()
snake = Snake()
food = Food()
control = Control(snake, food)

'''Главный цикл игры'''


def game_loop():
    while not control.game_closed:

        while control.game_over:
            control.game_over_menu()

        control.control(snake)
        control.is_alive(snake)

        window.background_fill()

        food.render()
        snake.render()
        Message.score_message(snake.length)
        Message.speed_message(snake.speed)

        window.update(snake.speed)

        snake.eat_food(food)

    pygame.quit()
    quit()


game_loop()
