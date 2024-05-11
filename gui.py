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
        pygame.time.Clock().tick(30)
        return pygame.display.update()
