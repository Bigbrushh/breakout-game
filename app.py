import pygame

pygame.init()

beige_marka = (250, 237, 201)
ford_dark_charcoal = (50, 50, 50)
black = (0, 0, 0)
dark_green = (0, 100, 0)
cornflower_blue = (100, 149, 237)

font = pygame.font.Font(None, 36)

screen_width = 800
screen_height = 600

ball_width = 10
ball_height = 10
ball_x = screen_width // 2 - ball_width // 2
ball_y = screen_height // 2 - ball_height // 2
ball_dx = 3
ball_dy = -3

paddle_width = 100
paddle_height = 10
paddle_x = screen_width // 2 - paddle_width // 2
paddle_y = screen_height - 40
paddle_dx = 0
paddle_speed = 6

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("벽돌 깨기 게임")

game_over = False


def reset_game():
    global ball_x, ball_y, ball_dx, ball_dy, paddle_x, game_over
    ball_x = screen_width // 2 - ball_width // 2
    ball_y = screen_height // 2 - ball_height // 2
    ball_dx = 3
    ball_dy = -3
    paddle_x = screen_width // 2 - paddle_width // 2
    game_over = False


running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle_dx = -paddle_speed
            if event.key == pygame.K_RIGHT:
                paddle_dx = paddle_speed
            if event.key == pygame.K_r and game_over:
                reset_game()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                paddle_dx = 0

    if not game_over:
        paddle_x += paddle_dx
        if paddle_x < 0:
            paddle_x = 0
        if paddle_x > screen_width - paddle_width:
            paddle_x = screen_width - paddle_width

        ball_x += ball_dx
        ball_y += ball_dy

        if ball_x <= 0 or ball_x >= screen_width - ball_width:
            ball_dx = -ball_dx
        if ball_y <= 0 or ball_y >= screen_height - ball_height:
            ball_dy = -ball_dy

        if ball_y >= screen_height - ball_height:
            game_over = True

    screen.fill(beige_marka)

    pygame.draw.ellipse(screen, ford_dark_charcoal, (ball_x, ball_y, ball_width, ball_height))

    paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
    pygame.draw.rect(screen, black, paddle_rect)

    if game_over:
        game_over_text = font.render("Game Over - Press 'R' to Restart", True, dark_green)
        screen.blit(game_over_text, (
            screen_width // 2 - game_over_text.get_width() // 2,
            screen_height // 2 - game_over_text.get_height() // 2
        ))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
