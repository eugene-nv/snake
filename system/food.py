from components.components import Color, Coordinate, Render, DisplaySize


class Food:

    def __init__(self):
        self.color = Color('food').color
        self.x = Coordinate('random', DisplaySize.width).coordinate
        self.y = Coordinate('random', DisplaySize.height).coordinate

    def render(self):
        '''Отрисовка еды'''
        Render.render(self.color, self.x, self.y)

    def update(self):
        '''Создание новой еды'''

        self.x = Coordinate('random', DisplaySize.width).coordinate
        self.y = Coordinate('random', DisplaySize.height).coordinate
