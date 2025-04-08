import pygame
from constants import WHITE_COLOR, BLACK_COLOR, WINDOW_WIDTH, WINDOW_HEIGHT


class Game:
    def __init__(self):
        """Init"""
        self.score1 = 0
        self.score2 = 0
        pygame.init()
        pygame.display.set_caption("Pong")
        self.font = pygame.font.SysFont("Courier", 24)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    def clear_screen(self):
        """clear screen"""
        self.screen.fill(BLACK_COLOR)

    def draw_scoreboard(self):
        """draw scoreboard"""
        score_text = self.font.render(
            f"Player 1: {self.score1}  Player 2: {self.score2}", True, WHITE_COLOR)
        self.screen.blit(score_text, (WINDOW_WIDTH // 2 -
                         score_text.get_width() // 2, 20))

    def increase_score(self, player):
        """increase score"""
        if player == "player1":
            self.score1 += 1
        else:
            self.score2 += 1

    def draw_rect(self, color, rect):
        """draw rect"""
        pygame.draw.rect(self.screen, color, rect)

    def draw_ellipse(self, color, rect):
        """draw an ellipse"""
        pygame.draw.ellipse(self.screen, color, rect)

    def update_board(self):
        """Update board"""
        # Update the display
        pygame.display.flip()
        # Control frame rate (60 FPS)
        self.clock.tick(60)

    def quit(self):
        """quit game"""
        # Quit Pygame
        pygame.quit()
