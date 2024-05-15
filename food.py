import random

import pygame

from gui import Window
from snake import Snake


class Food:

    def __init__(self):
        self.window = Window()
        self.snake = Snake()
        self.x = round(random.randrange(0, self.window.width - self.snake.block) / 10.0) * 10.0
        self.y = round(random.randrange(0, self.window.height - self.snake.block) / 10.0) * 10.0

    def render(self):
        pygame.draw.rect(self.window.main_window, (185, 49, 79), [self.x, self.y, self.snake.block, self.snake.block])

    def update(self):
        self.x = round(random.randrange(0, self.window.width - self.snake.block) / 10.0) * 10.0
        self.y = round(random.randrange(0, self.window.height - self.snake.block) / 10.0) * 10.0

