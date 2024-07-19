import pygame
pygame.init()

beige_marka = (250, 237, 201)

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("벽돌 깨기 게임")
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(beige_marka)

    pygame.display.flip()

pygame.quit()