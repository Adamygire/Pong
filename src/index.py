
import pygame
from constants import *
from service import Ball, Paddle
from ui import Game

def main():
    # Initialize Pygame
    game = Game()

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
        game.clear_screen()

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

        if ball.rect.colliderect(left_paddle.rect) or ball.rect.colliderect(right_paddle.rect):
            ball.flip_horizontal()

        # Scoring
        if ball.is_over_horizontal_edge(position='left'):
            game.increase_score("player2")
            ball.recenter()
            ball.flip_horizontal()

        if ball.is_over_horizontal_edge(position='right'):
            game.increase_score("player1")
            ball.recenter()
            ball.flip_horizontal()

        # Draw paddles, ball, and scoreboard
        game.draw_rect(WHITE_COLOR, left_paddle.rect)
        game.draw_rect(WHITE_COLOR, right_paddle.rect)
        game.draw_ellipse(WHITE_COLOR, ball.rect)

        # Scoreboard
        game.draw_scoreboard()

        game.update_board()

    # Quit Pygame
    pygame.quit()


if __name__ == '__main__':
    main()