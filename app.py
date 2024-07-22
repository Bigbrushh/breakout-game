import pygame
pygame.init()

beige_marka = (250, 237, 201)
ford_dark_charcoal = (50, 50, 50)

screen_width = 800
screen_height = 600

ball_width = 10
ball_height = 10
ball_x = screen_width // 2 - ball_width // 2
ball_y = screen_width // 2 - ball_height // 2
ball_dx = 3
ball_dy = -3

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("벽돌 깨기 게임")

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball_x += ball_dx
    ball_y += ball_dy

    if ball_x <= 0 or ball_x >= screen_width - ball_width:
        ball_dx = -ball_dx
    if ball_y <= 0 or ball_y >= screen_height - ball_height:
        ball_dy = -ball_dy

    screen.fill(beige_marka)

    pygame.draw.ellipse(screen, ford_dark_charcoal, (ball_x, ball_y, ball_width, ball_height))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
