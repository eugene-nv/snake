import pygame


class Snake:

    def __init__(self, window):
        self.window = window
        self.block = 10
        self.color = (58, 79, 65)
        self.start_coordinates = (self.window.width / 2, self.window.height / 2)

    def create(self):
        return pygame.draw.rect(self.window.main_window, self.color,
                                [self.start_coordinates[0], self.start_coordinates[1], self.block, self.block])
