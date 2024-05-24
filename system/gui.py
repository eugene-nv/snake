import pygame

import settings
from components.components import MainWindow, DisplaySize, Font, Score, Speed


class Window:
    def __init__(self):
        self.width = DisplaySize.width
        self.height = DisplaySize.height

        pygame.display.set_caption(settings.WINDOW_NAME)
        pygame.display.set_icon(pygame.image.load(settings.WINDOW_ICON))

    @staticmethod
    def background_fill():
        return MainWindow.window.fill(settings.BACKGROUND_COLOR)

    @staticmethod
    def update():
        pygame.time.Clock().tick(Speed.speed)
        return pygame.display.update()


class Message:
    pygame.init()
    window = Window()
    font_style = pygame.font.SysFont(Font.font, 20)

    @classmethod
    def endgame_message(cls):
        mess = cls.font_style.render('You loose! Press "ESCAPE" for quit or "SPACE" for play again.', True,
                                     settings.MESSAGE_COLOR)
        MainWindow.window.blit(mess, [DisplaySize.width / 6, DisplaySize.height / 4])
        cls.window.update()

    @classmethod
    def score_message(cls, snake_len):
        score = Score(snake_len - 1)
        value = cls.font_style.render("Your score: " + str(score.score), True, settings.MESSAGE_COLOR)
        MainWindow.window.blit(value, [10, 10])

    @classmethod
    def speed_message(cls):
        value = cls.font_style.render("Your speed: " + str(Speed.speed - settings.SNAKE_SPEED), True,
                                      settings.MESSAGE_COLOR)
        MainWindow.window.blit(value, [10, 40])

# class Score:
#     pygame.init()
#     window = Window()
#     score_font = pygame.font.SysFont(Font.font, 20)
#
#     @classmethod
#     def score(cls, score):
#         value = cls.score_font.render("Your Score: " + str(score), True, settings.MESSAGE_COLOR)
#         MainWindow.window.blit(value, [0, 0])
