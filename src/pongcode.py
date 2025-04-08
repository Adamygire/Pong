import pygame
import random


# Set up the display
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
BALL_SIZE = 20

class Paddle:
    def __init__(self, position='left'):
        width = 20
        height = 100

        if position is 'left':
            location = 50
        else:
            location = WINDOW_WIDTH - 50 - width
        self.rect = pygame.Rect(location, WINDOW_HEIGHT // 2 - height // 2, width, height)

class Ball:
    size = BALL_SIZE

    def __init__(self):
        self.rect = pygame.Rect(0, 0, Ball.size, Ball.size)
        self.recenter()
        self.dx = 2
        self.dy = 2

    def flip_horizontal(self):
            self.dx *= -1

    def flip_vertical(self):
            self.dy *= -1

    def is_over_vertical_edge(self):
        return self.rect.top <= 0 or self.rect.bottom >= WINDOW_HEIGHT

    def is_over_horizontal_edge(self, position='left'):
        passed_left_wall = self.rect.left < 0
        passed_right_wall = self.rect.right > WINDOW_WIDTH
        if position is 'left':
            return passed_left_wall
        elif position is 'right':
            return passed_right_wall
        else:
            return passed_left_wall or passed_right_wall
    
    def set_location(self, location):
        self.rect.x, self.rect.y = location

    def recenter(self):
        self.rect.x = WINDOW_WIDTH // 2 - Ball.size // 2
        self.rect.y = WINDOW_HEIGHT // 2 - Ball.size // 2

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy


def main():
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Pong")

    # Define colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

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
        if keys[down] and paddle.bottom < WINDOW_HEIGHT:
            paddle.y += 20

    left_paddle = Paddle(position='left')
    right_paddle = Paddle(position='right')
    ball = Ball()

    # Main game loop
    running = True
    while running:
        screen.fill(BLACK)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Move paddles
        move_paddle(left_paddle.rect, pygame.K_w, pygame.K_s)
        move_paddle(right_paddle.rect, pygame.K_UP, pygame.K_DOWN)

        ball.move()

        # Ball collisions with top and bottom
        if ball.is_over_vertical_edge():
            ball.flip_vertical()
            pygame.mixer.Sound("./sounds/bounce.mp3").play()

        if ball.rect.colliderect(left_paddle.rect) or ball.rect.colliderect(right_paddle.rect):
            ball.flip_horizontal()
            pygame.mixer.Sound("./sounds/bounce.mp3").play()

        # Scoring
        if ball.is_over_horizontal_edge(position='left'):
            score2 += 1
            ball.recenter()
            ball.flip_horizontal()
            pygame.mixer.Sound("./sounds/bounce.mp3").play()

        if ball.is_over_horizontal_edge(position='right'):
            score1 += 1
            ball.recenter()
            ball.flip_horizontal()
            pygame.mixer.Sound("./sounds/bounce.mp3").play()

        # Draw paddles, ball, and scoreboard
        pygame.draw.rect(screen, WHITE, left_paddle.rect)
        pygame.draw.rect(screen, WHITE, right_paddle.rect)
        pygame.draw.ellipse(screen, WHITE, ball.rect)

        # Scoreboard
        score_text = font.render(f"Player 1: {score1}  Player 2: {score2}", True, WHITE)
        screen.blit(score_text, (WINDOW_WIDTH // 2 - score_text.get_width() // 2, 20))

        # Update the display
        pygame.display.flip()

        # Control frame rate (60 FPS)
        clock.tick(60)

    # Quit Pygame
    pygame.quit()


if __name__ == '__main__':
    main()