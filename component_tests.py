import unittest

import pygame

import settings
from components.components import Block, Color, Coordinate, DisplaySize, MainWindow, Render, Font, Score, Speed
from system.snake import Snake


class BlockComponentTestCase(unittest.TestCase):

    def setUp(self):
        self.block = Block()

    def test_block(self):
        self.assertEqual(self.block.size, settings.BLOCK_SIZE)
        self.assertEqual(type(self.block.size), int)


class ColorComponentTestCase(unittest.TestCase):

    def setUp(self):
        self.color = Color()
        self.snake_color = Color('snake')
        self.food_color = Color('food')
        self.background_color = Color('background')
        self.message_color = Color('message')

    def test_color_type(self):
        self.assertEqual(type(self.color.color), tuple)

    def test_snake_color(self):
        self.assertEqual(self.snake_color.color, settings.SNAKE_COLOR)

    def test_food_color(self):
        self.assertEqual(self.food_color.color, settings.FOOD_COLOR)

    def test_background_color(self):
        self.assertEqual(self.background_color.color, settings.BACKGROUND_COLOR)

    def test_message_color(self):
        self.assertEqual(self.message_color.color, settings.MESSAGE_COLOR)


class CoordinateTestCase(unittest.TestCase):
    def setUp(self):
        self.snake = Snake()

        self.random_coordinate_x = Coordinate(creation='random', axis=DisplaySize.width)
        self.random_coordinate_y = Coordinate(creation='random', axis=DisplaySize.height)
        self.center_coordinate_x = Coordinate(creation='center', axis=DisplaySize.width)
        self.center_coordinate_y = Coordinate(creation='center', axis=DisplaySize.height)

    def test_center_coordinate(self):
        self.assertEqual(self.center_coordinate_x.coordinate, settings.WIDTH / 2)
        self.assertEqual(self.center_coordinate_y.coordinate, settings.HEIGHT / 2)

    def test_random_coordinate(self):
        self.assertEqual(self.random_coordinate_x.coordinate < settings.WIDTH, True)
        self.assertEqual(self.random_coordinate_y.coordinate < settings.HEIGHT, True)

        self.assertEqual(self.random_coordinate_x.coordinate > 0, True)
        self.assertEqual(self.random_coordinate_y.coordinate > 0, True)

    def test_change_coordinate(self):
        Coordinate.change(self.snake, 10, 10)

        self.assertEqual(self.snake.x == settings.WIDTH / 2 + 10, True)
        self.assertEqual(self.snake.y == settings.HEIGHT / 2 + 10, True)


class MainWindowTestCase(unittest.TestCase):
    def setUp(self):
        self.main_window = MainWindow()

    def test_main_window(self):
        self.assertEqual(isinstance(self.main_window.window, pygame.surface.Surface), True)


class RenderTestCase(unittest.TestCase):
    pass


class DisplaySizeTestCase(unittest.TestCase):
    def setUp(self):
        self.width = DisplaySize.width
        self.height = DisplaySize.height

    def test_display_size(self):
        self.assertEqual(self.width, settings.WIDTH)
        self.assertEqual(self.height, settings.HEIGHT)


class FontTestCase(unittest.TestCase):
    def setUp(self):
        self.font = Font.font

    def test_font(self):
        self.assertEqual(self.font, settings.FONT)


class ScoreTestCase(unittest.TestCase):
    def setUp(self):
        self.score = Score(1).score

    def test_score(self):
        self.assertEqual(self.score, 1)
        self.assertEqual(type(self.score), int)


class SpeedTestCase(unittest.TestCase):
    def setUp(self):
        self.speed = Speed

    def test_speed(self):
        self.assertEqual(self.speed.speed, settings.SNAKE_SPEED)
        self.assertEqual(type(self.speed.speed), int)

    def add_speed(self):
        self.speed.add_speed()
        self.assertEqual(self.speed.speed, settings.SNAKE_SPEED + 1)

    def rest_speed(self):
        self.speed.add_speed()
        self.speed.reset()
        self.assertEqual(self.speed.speed, settings.SNAKE_SPEED)


if __name__ == '__main__':
    unittest.main()
