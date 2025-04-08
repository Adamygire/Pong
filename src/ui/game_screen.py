import pygame
from constants import WHITE_COLOR, BLACK_COLOR, WINDOW_WIDTH, WINDOW_HEIGHT


class GameScreen:
    def __init__(self):
        """Init"""
        pygame.init()
        pygame.display.set_caption("Pong")
        self.font = pygame.font.SysFont("Courier", 24)
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    def clear_screen(self):
        """clear screen"""
        self.screen.fill(BLACK_COLOR)

    def draw_scoreboard(self, score1, score2):
        """draw scoreboard"""
        score_text = self.font.render(
            f"Player 1: {score1}  Player 2: {score2}", True, WHITE_COLOR)
        self.screen.blit(score_text, (WINDOW_WIDTH // 2 -
                         score_text.get_width() // 2, 20))
