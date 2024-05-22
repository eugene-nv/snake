import random

import pygame

import settings
from components.components import Block, DisplaySize, Coordinate
from system.gui import Message


class Control:
    def __init__(self, snake, food):
        self.game_closed = False
        self.game_over = False
        self.snake = snake
        self.closed_border = True
        self.food = food

    def control(self, snake):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_closed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.shift_x = -Block.size
                    snake.shift_y = 0
                elif event.key == pygame.K_RIGHT:
                    snake.shift_x = Block.size
                    snake.shift_y = 0
                elif event.key == pygame.K_UP:
                    snake.shift_y = -Block.size
                    snake.shift_x = 0
                elif event.key == pygame.K_DOWN:
                    snake.shift_y = Block.size
                    snake.shift_x = 0

        snake.x += snake.shift_x
        snake.y += snake.shift_y

    def is_alive(self, snake):

        for x in snake.list[:-1]:
            if x == snake.head:
                self.game_over = True

        if self.closed_border:
            if (self.snake.x >= DisplaySize.width or self.snake.x < 0 or self.snake.y >= DisplaySize.height or
                    self.snake.y < 0):
                self.game_over = True
        else:
            if self.snake.x >= DisplaySize.width:
                self.snake.x = 0
            elif self.snake.x == 0:
                self.snake.x = DisplaySize.width
            elif self.snake.y >= DisplaySize.height:
                self.snake.y = 0
            elif self.snake.y == 0:
                self.snake.y = DisplaySize.height

    def new_game(self):
        self.game_closed = False
        self.game_over = False
        self.snake.x = DisplaySize.width / 2
        self.snake.y = DisplaySize.height / 2
        self.snake.list = []
        self.snake.length = 1
        self.snake.head = []
        self.food.x = Coordinate(creation='random', axis=DisplaySize.width).coordinate
        self.food.y = Coordinate(creation='random', axis=DisplaySize.height).coordinate

    def end_game(self):
        self.game_closed = True
        self.game_over = False

    def game_over_menu(self):
        Message.message('You loose! Press "ESCAPE" for quit or "SPACE" for play again.')
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.end_game()
                if event.key == pygame.K_SPACE:
                    self.new_game()
