import unittest

import pygame

from system.gui import Window
from system.snake import Snake


# class WindowTestCase(unittest.TestCase):
#     def setUp(self):
#         self.window = Window()
#
#     def test_window(self):
#         self.assertEqual(self.window.width, 800)
#         self.assertEqual(self.window.height, 600)
#         self.assertEqual(self.window.background_color, (225, 222, 227))
#         self.assertEqual(isinstance(self.window.main_window, pygame.surface.Surface), True)
#         self.assertEqual(isinstance(self.window.background_fill(), pygame.rect.Rect), True)
#
#
# class SnakeTestCase(unittest.TestCase):
#     def setUp(self):
#         self.window = Window()
#         self.snake = Snake()
#
#     def test_snake(self):
#         self.assertEqual(self.snake.block, 10)
#         self.assertEqual(self.snake.color, (58, 79, 65))
#         self.assertEqual(self.snake.x, self.window.width / 2)
#         self.assertEqual(self.snake.y, self.window.height / 2)
#         self.assertEqual(self.snake.change_x, 0)
#         self.assertEqual(self.snake.change_y, 0)
#
#         self.assertEqual(isinstance(self.snake.render(), pygame.rect.Rect), True)
#

if __name__ == '__main__':
    unittest.main()
