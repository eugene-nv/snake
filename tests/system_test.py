import unittest

import settings
from components.components import Speed, DisplaySize
from system.control import Control
from system.gui import Window
from system.snake import Snake
from system.food import Food


class SnakeTestCase(unittest.TestCase):
    def setUp(self):
        self.snake = Snake()

    def test_snake(self):
        self.assertEqual(self.snake.block, settings.BLOCK_SIZE)
        self.assertEqual(self.snake.color, settings.SNAKE_COLOR)
        self.assertEqual(self.snake.x, settings.WIDTH / 2)
        self.assertEqual(self.snake.y, settings.HEIGHT / 2)
        self.assertEqual(self.snake.shift_x, 0)
        self.assertEqual(self.snake.shift_y, 0)
        self.assertEqual(self.snake.list, [])
        self.assertEqual(self.snake.head, [])
        self.assertEqual(self.snake.length, 1)
        self.assertEqual(self.snake.speed, Speed().speed)

    def test_snake_render(self):
        self.assertEqual(self.snake.head, [])

        self.snake.render()

        self.assertEqual(self.snake.head, [settings.WIDTH / 2, settings.HEIGHT / 2])
        self.assertEqual(self.snake.list, [[settings.WIDTH / 2, settings.HEIGHT / 2]])
        self.assertEqual(len(self.snake.list) <= self.snake.length, True)

    def test_eat_food(self):
        food = Food()

        food.x = 400.0
        food.y = 300.0

        self.snake.eat_food(food)

        self.assertEqual(self.snake.speed, 11)
        self.assertEqual(self.snake.length, 2)

        food.x = 401.0
        food.y = 301.0

        self.snake.x += 1
        self.snake.y += 1

        self.snake.eat_food(food)

        self.assertEqual(self.snake.speed, 12)
        self.assertEqual(self.snake.length, 3)


class FoodTestCase(unittest.TestCase):
    def setUp(self):
        self.food = Food()

    def food_test_case(self):
        self.assertEqual(self.food.color, settings.FOOD_COLOR)

        self.assertEqual(self.food.x < settings.WIDTH, True)
        self.assertEqual(self.food.y < settings.HEIGHT, True)

        self.assertEqual(self.food.x > 0, True)
        self.assertEqual(self.food.y > 0, True)

    def test_food_render(self):
        pass

    def test_update_food_coordinate(self):
        x = self.food.x
        y = self.food.y

        self.food.update()
        self.assertEqual((x, y) != (self.food.x, self.food.y), True)


class ControlTestCase(unittest.TestCase):
    def setUp(self):
        self.snake = Snake()
        self.food = Food()
        self.control = Control(self.snake, self.food)

    def test_control(self):
        self.assertEqual(self.control.game_over, False)
        self.assertEqual(self.control.game_closed, False)
        self.assertEqual(self.control.closed_border, settings.CLOSED_BORDERS)

    def test_pygame_event(self):
        pass

    def test_is_alive(self):
        self.snake.render()
        self.control.is_alive(self.snake)
        self.assertEqual(self.control.game_over, False)

    def test_new_game(self):
        self.control.new_game()

        self.assertEqual(self.control.game_closed, False)
        self.assertEqual(self.control.game_over, False)
        self.assertEqual(self.control.snake.x, DisplaySize.width / 2)
        self.assertEqual(self.control.snake.y, DisplaySize.height / 2)
        self.assertEqual(self.control.snake.list, [])
        self.assertEqual(self.control.snake.length, 1)
        self.assertEqual(self.control.snake.head, [])
        self.assertEqual(self.control.snake.speed, settings.SNAKE_SPEED)
        self.assertEqual(self.control.food.x < settings.WIDTH, True)
        self.assertEqual(self.control.food.y < settings.HEIGHT, True)

    def test_end_game(self):
        self.control.end_game()
        self.assertEqual(self.control.game_over, False)
        self.assertEqual(self.control.game_closed, True)

    def test_game_over_menu(self):
        pass


class WindowTestCase(unittest.TestCase):
    def setUp(self):
        self.window = Window()

    def test_window(self):
        self.assertEqual(self.window.width, settings.WIDTH)
        self.assertEqual(self.window.height, settings.HEIGHT)


if __name__ == '__main__':
    unittest.main()
