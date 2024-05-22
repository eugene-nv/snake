import pygame

import settings
from components.components import MainWindow, DisplaySize, Font


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
        pygame.time.Clock().tick(settings.SNAKE_SPEED)
        return pygame.display.update()


class Message:
    pygame.init()
    window = Window()
    font_style = pygame.font.SysFont(Font.font, 20)

    @classmethod
    def message(cls, text):
        mess = cls.font_style.render(text, True, (213, 161, 142))
        MainWindow.window.blit(mess, [DisplaySize.width / 6, DisplaySize.height / 4])
        cls.window.update()


class Score:
    pygame.init()
    window = Window()
    score_font = pygame.font.SysFont(Font.font, 20)

    @classmethod
    def score(cls, score):
        value = cls.score_font.render("Your Score: " + str(score), True, (255, 255, 102))
        MainWindow.window.blit(value, [0, 0])
