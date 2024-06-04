from components.components import Block, Color, Coordinate, Render, DisplaySize, Speed


class Snake:

    def __init__(self):
        self.block = Block.size
        self.color = Color('snake').color
        self.x = Coordinate('center', DisplaySize.width).coordinate
        self.y = Coordinate('center', DisplaySize.height).coordinate
        self.shift_x = 0
        self.shift_y = 0
        self.list = []
        self.length = 1
        self.head = []
        self.speed = Speed.speed

    def render(self):

        '''Отрисовка змейки'''

        self.head = []
        self.head.append(self.x)
        self.head.append(self.y)
        self.list.append(self.head)

        '''Удаление последнего блока змейки для имитации движения'''

        if len(self.list) > self.length:
            del self.list[0]

        for i in self.list:
            Render.render(self.color, i[0], i[1])

    def eat_food(self, food):

        '''Змейка ест еду'''

        if self.x == food.x and self.y == food.y:
            food.update()
            self.length += 1
            self.speed = Speed.add_speed(self.speed)
