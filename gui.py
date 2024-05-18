import pygame


class Window:

    def __init__(self):
        self.width = 800
        self.height = 600
        self.background_color = (225, 222, 227)
        self.main_window = pygame.display.set_mode((self.width, self.height))

        pygame.display.set_caption('Snake')
        pygame.display.set_icon(pygame.image.load('icon.png'))

    def background_fill(self):
        return self.main_window.fill(self.background_color)

    @staticmethod
    def update():
        pygame.time.Clock().tick(20)
        return pygame.display.update()


class Message:
    pygame.init()
    window = Window()
    font_style = pygame.font.SysFont('Calibri', 20)

    @classmethod
    def message(cls, text):
        mess = cls.font_style.render(text, True, (213, 161, 142))
        cls.window.main_window.blit(mess, [cls.window.width / 6, cls.window.height / 4])
        cls.window.update()


class Score:
    pygame.init()
    window = Window()
    score_font = pygame.font.SysFont("comicsansms", 20)

    @classmethod
    def score(cls, score):
        value = cls.score_font.render("Your Score: " + str(score), True, (255, 255, 102))
        cls.window.main_window.blit(value, [0, 0])