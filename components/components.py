import random
from dataclasses import dataclass

import pygame

import settings


@dataclass
class Block:
    '''Размер блока'''

    size: int = settings.BLOCK_SIZE


@dataclass
class Color:
    '''Цвет для элемента'''

    obj: str = None
    color: tuple = None

    def __post_init__(self):
        if self.obj == 'snake':
            self.color = settings.SNAKE_COLOR
        elif self.obj == 'food':
            self.color = settings.FOOD_COLOR
        elif self.obj == 'background':
            self.color = settings.BACKGROUND_COLOR
        elif self.obj == 'message':
            self.color = settings.MESSAGE_COLOR
        else:
            self.color = (255, 255, 255)


@dataclass
class Coordinate:
    '''Координаты для элемента'''

    creation: str = None
    axis: int = None
    coordinate: float = None

    @staticmethod
    def change(snake, shift_x, shift_y):
        '''Смена координат для элемента'''

        snake.x += shift_x
        snake.y += shift_y

    def __post_init__(self):
        if self.creation and self.axis:
            if self.creation == 'random':
                self.coordinate = round(random.randrange(0, self.axis - settings.BLOCK_SIZE) / 10.0) * 10.0
            elif self.creation == 'center':
                self.coordinate = self.axis / 2


@dataclass
class MainWindow:
    '''Создание главного окна игры'''

    window = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))


@dataclass
class Render:
    '''Отрисовка элемента'''
    @staticmethod
    def render(color, x, y):
        pygame.draw.rect(MainWindow.window, color, [x, y, Block.size, Block.size])


@dataclass
class DisplaySize:
    '''Размер игрового окна'''

    width: int = settings.WIDTH
    height: int = settings.HEIGHT


@dataclass
class Font:
    '''Шрифт'''

    font: str = settings.FONT


@dataclass
class Score:
    '''Набранные очки'''

    score: int


@dataclass
class Speed:
    '''Скорость змейки'''

    speed: int = settings.SNAKE_SPEED

    @staticmethod
    def add_speed(speed):
        '''Увеичение скорости змейки'''

        speed += 1
        return speed

    @staticmethod
    def reset():
        '''Обнуление скорости змейки'''

        return settings.SNAKE_SPEED
