import pygame

from gui import Window


class Snake:

    def __init__(self):
        self.window = Window()
        self.block = 10
        self.color = (58, 79, 65)
        self.x = self.window.width / 2
        self.y = self.window.height / 2
        self.change_x = 0
        self.change_y = 0

    def render(self):
        return pygame.draw.rect(self.window.main_window, self.color,
                                [self.x, self.y, self.block, self.block])
