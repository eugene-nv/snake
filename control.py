import pygame


class Control:
    def __init__(self):
        self.game_over = False

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
