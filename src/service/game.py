import pygame
from .ball import Ball
from .paddle import Paddle


class Game:
    def __init__(self, use_ai=False, game_screen=None):
        """Initialize the game"""
        self.use_ai = use_ai
        self.score1 = 0
        self.score2 = 0
        self.clock = pygame.time.Clock()
        self.game_screen = game_screen

        self.bounce_sound = pygame.mixer.Sound("./sounds/bounce.mp3")
        self.ball = Ball(self.game_screen.screen)
        self.left_paddle = Paddle(self.game_screen.screen, position='left')
        self.right_paddle = Paddle(
            self.game_screen.screen,
            position='right',
            is_ai=self.use_ai,
            ball=self.ball if self.use_ai else None
        )

    def handle_collisions(self):
        """Handle collisions in the game"""
        self.ball.handle_collision_with_vertical_edge()
        collided_with_left = self.ball.has_collided(self.left_paddle.rect)
        collided_with_right = self.ball.has_collided(self.right_paddle.rect)
        if collided_with_left or collided_with_right:
            self.ball.flip_horizontal()
            self.bounce_sound.play()

    def handle_scoring(self):
        """Handle scoring in the game"""
        if self.ball.is_out_of_bounds(position='left'):
            self.score2 += 1
            self.ball.recenter()
            self.ball.flip_horizontal()
            self.bounce_sound.play()

        if self.ball.is_out_of_bounds(position='right'):
            self.score1 += 1
            self.ball.recenter()
            self.ball.flip_horizontal()
            self.bounce_sound.play()

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

    def handle_game_over(self):
        if self.score1 >= 5 or self.score2 >= 5:
            winner = "Player 1" if self.score1 >= 5 else "Player 2"
            self.game_screen.show_game_over_screen(winner)
            self.reset_game()

    def reset_game(self):
        self.score1 = 0
        self.score2 = 0
        self.ball.recenter()
        self.ball.flip_horizontal()

    def play(self):
        """Main game loop"""
        running = True
        while running:
            self.game_screen.clear_screen()
            self.handle_collisions()
            self.handle_scoring()
            self.move_pieces()
            self.handle_game_over()
            self.draw_pieces()

            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()
