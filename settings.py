import os

BLOCK_SIZE = 10

SNAKE_COLOR = (58, 79, 65)
FOOD_COLOR = (185, 49, 79)
BACKGROUND_COLOR = (244, 245, 235)
MESSAGE_COLOR = (32, 7, 114)

WIDTH = 800
HEIGHT = 600

WINDOW_NAME = 'Snake'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WINDOW_ICON = os.path.join(BASE_DIR, 'snake/media/icon.png')

SNAKE_SPEED = 10

FONT = 'comicsansms'

CLOSED_BORDERS = True
