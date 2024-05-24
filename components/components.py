import random
from dataclasses import dataclass

import pygame

import settings


@dataclass
class Block:
    size: int = settings.BLOCK_SIZE


@dataclass
class Color:
    color: tuple = None


@dataclass
class Coordinate:
    creation: str = None
    axis: int = None
    coordinate: float = None

    @staticmethod
    def change(snake, shift_x, shift_y):
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
    window = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))


@dataclass
class Render:
    @staticmethod
    def render(color, x, y):
        pygame.draw.rect(MainWindow.window, color, [x, y, Block.size, Block.size])


@dataclass
class DisplaySize:
    width: int = settings.WIDTH
    height: int = settings.HEIGHT


@dataclass
class Font:
    font: str = settings.FONT


@dataclass
class Score:
    score: int


@dataclass
class Speed:
    speed: int = settings.SNAKE_SPEED

    @classmethod
    def add_speed(cls):
        cls.speed += 1

    @classmethod
    def reset(cls):
        cls.speed = settings.SNAKE_SPEED
