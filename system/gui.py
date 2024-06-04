import pygame

import settings
from components.components import MainWindow, DisplaySize, Font, Score, Color


class Window:
    def __init__(self):
        self.width = DisplaySize.width
        self.height = DisplaySize.height

        pygame.display.set_caption(settings.WINDOW_NAME)
        pygame.display.set_icon(pygame.image.load(settings.WINDOW_ICON))

    @staticmethod
    def background_fill():
        '''Заливка фона цветом'''

        return MainWindow.window.fill(Color('background').color)

    @staticmethod
    def update(snake_speed):
        '''Обновление экрана'''

        pygame.time.Clock().tick(snake_speed)
        return pygame.display.update()


class Message:
    pygame.init()
    window = Window()
    font_style = pygame.font.SysFont(Font.font, 20)

    @classmethod
    def endgame_message(cls, snake_speed):
        '''Сообщение при пройгрыше'''

        mess = cls.font_style.render('You loose! Press "ESCAPE" for quit or "SPACE" for play again.', True,
                                     Color('message').color)
        MainWindow.window.blit(mess, [DisplaySize.width / 6, DisplaySize.height / 4])
        cls.window.update(snake_speed)

    @classmethod
    def score_message(cls, snake_len):
        '''Отрисовка набранных очков'''

        score = Score(snake_len - 1)
        value = cls.font_style.render("Score: " + str(score.score), True, Color('message').color)
        MainWindow.window.blit(value, [10, 10])

    @classmethod
    def speed_message(cls, snake_speed):
        '''Отрисовка текущей скорости змейки'''

        value = cls.font_style.render("Speed: " + str(snake_speed - settings.SNAKE_SPEED), True,
                                      Color('message').color)
        MainWindow.window.blit(value, [10, 40])
