import pygame

pygame.init()

window = pygame.display.set_mode((800, 600))

'''Главный цикл игры'''

game_over = False
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    window.fill((255, 255, 255))
    pygame.display.update()

pygame.quit()
quit()


