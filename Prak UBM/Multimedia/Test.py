import pygame, sys

pygame.init()

WIDTH = 900
HEIGHT = 600
Red_color = (255, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
game_over = False

while not game_over:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.draw.rect(screen, Red_color, (100, 500, 50, 50))
    pygame.display.update()