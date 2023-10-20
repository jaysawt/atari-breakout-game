import pygame
import random

# Initialize Pygame
pygame.init()

# Game constants
WIDTH, HEIGHT = 640, 480
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 10
BALL_RADIUS = 8
BRICK_WIDTH, BRICK_HEIGHT = 64, 20
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Create the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout")

# Clock for controlling frame rate
clock = pygame.time.Clock()

def create_bricks():
    bricks = []
    for row in range(5):
        for col in range(WIDTH // BRICK_WIDTH):
            brick_x = col * BRICK_WIDTH
            brick_y = row * BRICK_HEIGHT + 50
            brick_rect = pygame.Rect(brick_x, brick_y, BRICK_WIDTH, BRICK_HEIGHT)
            bricks.append(brick_rect)
    return bricks

def draw_bricks(bricks):
    for brick in bricks:
        pygame.draw.rect(window, BLUE, brick)

def draw_paddle(paddle):
    pygame.draw.rect(window, RED, paddle)

def draw_ball(ball):
    pygame.draw.circle(window, RED, (ball.x, ball.y), BALL_RADIUS)

def game_over():
    font = pygame.font.Font(None, 50)
    text = font.render("Game Over", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    window.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.delay(2000)
    pygame.quit()
    quit()

def main():
    paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 20, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, 2 * BALL_RADIUS, 2 * BALL_RADIUS)
    ball_speed_x = 5
    ball_speed_y = -5

    bricks = create_bricks()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.left > 0:
            paddle.x -= 7
        if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
            paddle.x += 7

        ball.x += ball_speed_x
        ball.y += ball_speed_y

        if ball.left <= 0 or ball.right >= WIDTH:
            ball_speed_x *= -1
        if ball.top <= 0:
            ball_speed_y *= -1
        if ball.bottom >= HEIGHT:
            game_over()

        if ball.colliderect(paddle):
            ball_speed_y *= -1

        brick_hit_index = ball.collidelist(bricks)
        if brick_hit_index != -1:
            brick = bricks[brick_hit_index]
            bricks.pop(brick_hit_index)
            if ball.colliderect(brick):
                if ball.centerx < brick.left or ball.centerx > brick.right:
                    ball_speed_x *= -1
                else:
                    ball_speed_y *= -1

        window.fill((0, 0, 0))
        draw_bricks(bricks)
        draw_paddle(paddle)
        draw_ball(ball)
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()