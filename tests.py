import unittest

import pygame

from gui import Window


class WindowTestCase(unittest.TestCase):
    def setUp(self):
        self.window = Window()

    def test_window(self):
        self.assertEqual(self.window.width, 800)
        self.assertEqual(self.window.height, 600)
        self.assertEqual(self.window.background_color, (255, 255, 255))
        self.assertEqual(isinstance(self.window.main_window, pygame.surface.Surface), True)
        self.assertEqual(isinstance(self.window.background_fill(), pygame.rect.Rect), True)


if __name__ == '__main__':
    unittest.main()
