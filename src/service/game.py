import pygame
from ui import GameScreen
from .ball import Ball
from .paddle import Paddle


class Game:
    def __init__(self):
        """Init"""
        self.score1 = 0
        self.score2 = 0
        self.clock = pygame.time.Clock()
        self.game_screen = GameScreen()
        self.ball = Ball(self.game_screen.screen)
        self.left_paddle = Paddle(self.game_screen.screen, position='left')
        self.right_paddle = Paddle(self.game_screen.screen, position='right')

    def handle_collisions(self):
        self.ball.handle_collision_with_vertical_edge()
        collided_with_left = self.ball.has_collided(self.left_paddle.rect)
        collided_with_right = self.ball.has_collided(self.right_paddle.rect)
        if collided_with_left or collided_with_right:
            self.ball.flip_horizontal()

    def handle_scoring(self):
        if self.ball.is_out_of_bounds(position='left'):
            self.score2 += 1
            self.ball.recenter()
            self.ball.flip_horizontal()

        if self.ball.is_out_of_bounds(position='right'):
            self.score1 += 1
            self.ball.recenter()
            self.ball.flip_horizontal()

    def move_pieces(self):
        self.ball.move()
        self.left_paddle.move()
        self.right_paddle.move()

    def draw_pieces(self):
        self.left_paddle.draw()
        self.right_paddle.draw()
        self.ball.draw()
        self.game_screen.draw_scoreboard(self.score1, self.score2)
        pygame.display.flip()

    def play(self):
        """play game"""
        self.game_screen.wait_for_start()
        running = True
        while running:
            self.game_screen.clear_screen()
            self.move_pieces()
            self.handle_collisions()
            self.handle_scoring()
            self.move_pieces()
            self.draw_pieces()

            self.clock.tick(60)

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()
