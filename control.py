import random

import pygame
from gui import Message


class Control:
    def __init__(self, snake, food, window):
        self.game_closed = False
        self.game_over = False
        self.snake = snake
        self.closed_border = True
        self.window = window
        self.food = food

    def control(self, snake):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_closed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.change_x = -10
                    snake.change_y = 0
                elif event.key == pygame.K_RIGHT:
                    snake.change_x = 10
                    snake.change_y = 0
                elif event.key == pygame.K_UP:
                    snake.change_y = -10
                    snake.change_x = 0
                elif event.key == pygame.K_DOWN:
                    snake.change_y = 10
                    snake.change_x = 0

        snake.x += snake.change_x
        snake.y += snake.change_y

    def is_alive(self, window, snake):

        for x in snake.list[:-1]:
            if x == snake.head:
                self.game_over = True

        if self.closed_border:
            if self.snake.x >= window.width or self.snake.x < 0 or self.snake.y >= window.height or self.snake.y < 0:
                self.game_over = True
        else:
            if self.snake.x >= window.width:
                self.snake.x = 0
            elif self.snake.x == 0:
                self.snake.x = window.width
            elif self.snake.y >= window.height:
                self.snake.y = 0
            elif self.snake.y == 0:
                self.snake.y = window.height

    def new_game(self):
        self.game_closed = False
        self.game_over = False
        self.snake.x = self.window.width / 2
        self.snake.y = self.window.height / 2
        self.snake.list = []
        self.snake.length = 1
        self.snake.head = []
        self.food.x = round(random.randrange(0, self.window.width - self.snake.block) / 10.0) * 10.0
        self.food.y = round(random.randrange(0, self.window.height - self.snake.block) / 10.0) * 10.0

    def end_game(self):
        self.game_closed = True
        self.game_over = False

    def game_over_menu(self):
        Message.message("You loose! Press ESCAPE for quit or 'SPACE' for play again.")
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.end_game()
                if event.key == pygame.K_SPACE:
                    self.new_game()
