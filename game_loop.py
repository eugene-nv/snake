import pygame
from gui import Window

pygame.init()

window = Window()

'''Главный цикл игры'''

game_over = False
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    window.background_fill()
    window.update()

pygame.quit()
quit()


