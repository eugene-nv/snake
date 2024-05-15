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
        self.list = []
        self.length = 1
        self.head = []

    def render(self):
        self.head = []
        self.head.append(self.x)
        self.head.append(self.y)
        self.list.append(self.head)
        if len(self.list) > self.length:
            del self.list[0]

        for i in self.list:
            pygame.draw.rect(self.window.main_window, self.color,
                                [i[0], i[1], self.block, self.block])

    def eat_food(self, food):
        if self.x == food.x and self.y == food.y:
            food.update()
            print("Yummy!!")
            self.length += 1
