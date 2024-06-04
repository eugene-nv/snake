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
            '''Меню при пройгрыше'''
            control.game_over_menu()

        '''Управление змейкой'''
        control.control(snake)

        '''Проверка на пройгрыш'''
        control.is_alive(snake)

        '''Заливка фона цветом'''
        window.background_fill()

        '''Отрисовка еды'''
        food.render()

        '''Отрисовка змейки'''
        snake.render()

        '''Отрисовка набранных очков'''
        Message.score_message(snake.length)

        '''Отрисовка скорости змейки'''
        Message.speed_message(snake.speed)

        '''Обновление экрана'''
        window.update(snake.speed)

        '''Змейка ест еду'''
        snake.eat_food(food)

    pygame.quit()
    quit()


game_loop()
