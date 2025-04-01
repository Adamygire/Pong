import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the paddles and ball
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
BALL_SIZE = 20

paddle1 = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2 = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

# Set the initial ball direction and speed
ball_dx = 0.2
ball_dy = 0.2

# Initialize the scores
score1 = 0
score2 = 0

# Set up the font for the scoreboard
font = pygame.font.SysFont("Courier", 24)

# Initialize clock for controlling frame rate
clock = pygame.time.Clock()

# Function to move paddles
def move_paddle(paddle, up, down):
    keys = pygame.key.get_pressed()
    if keys[up] and paddle.top > 0:
        paddle.y -= 20
    if keys[down] and paddle.bottom < HEIGHT:
        paddle.y += 20

# Main game loop
running = True
while running:
    screen.fill(BLACK)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move paddles
    move_paddle(paddle1, pygame.K_w, pygame.K_s)
    move_paddle(paddle2, pygame.K_UP, pygame.K_DOWN)

    # Move the ball
    ball.x += ball_dx
    ball.y += ball_dy

    # Ball collisions with top and bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy *= -1
        pygame.mixer.Sound("bounce.wav").play()
        
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_dx *= -1
        pygame.mixer.Sound("bounce.wav").play()

    # Scoring
    if ball.left <= 0:
        score2 += 1
        ball.x = WIDTH // 2 - BALL_SIZE // 2
        ball_dx *= -1
        pygame.mixer.Sound("bounce.wav").play()

    if ball.right >= WIDTH:
        score1 += 1
        ball.x = WIDTH // 2 - BALL_SIZE // 2
        ball_dx *= -1
        pygame.mixer.Sound("bounce.wav").play()

    # Draw paddles, ball, and scoreboard
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Scoreboard
    score_text = font.render(f"Player 1: {score1}  Player 2: {score2}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

    # Update the display
    pygame.display.flip()

    # Control frame rate (60 FPS)
    clock.tick(60)

# Quit Pygame
pygame.quit()
