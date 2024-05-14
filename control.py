import pygame


class Control:
    def __init__(self, player):
        self.game_over = False
        self.player = player
        self.closed_border = True

    def control(self, player):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.change_x = -10
                    player.change_y = 0
                elif event.key == pygame.K_RIGHT:
                    player.change_x = 10
                    player.change_y = 0
                elif event.key == pygame.K_UP:
                    player.change_y = -10
                    player.change_x = 0
                elif event.key == pygame.K_DOWN:
                    player.change_y = 10
                    player.change_x = 0

        player.x += player.change_x
        player.y += player.change_y

    def is_alive(self, window):
        if self.closed_border:
            if self.player.x >= window.width or self.player.x < 0 or self.player.y >= window.height or self.player.y < 0:
                self.game_over = True
        else:
            if self.player.x >= window.width:
                self.player.x = 0
            elif self.player.x == 0:
                self.player.x = window.width
            elif self.player.y >= window.height:
                self.player.y = 0
            elif self.player.y == 0:
                self.player.y = window.height
