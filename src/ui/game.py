import pygame
from constants import *

class Game:
    def __init__(self):
        self.score1=0
        self.score2=0
        pygame.init()
        pygame.display.set_caption("Pong")
        self.font = pygame.font.SysFont("Courier", 24)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    def clear_screen(self):
        self.screen.fill(BLACK_COLOR)


    def draw_scoreboard(self):
        score_text = self.font.render(f"Player 1: {self.score1}  Player 2: {self.score2}", True, WHITE_COLOR)
        self.screen.blit(score_text, (WINDOW_WIDTH // 2 - score_text.get_width() // 2, 20))

    def increase_score(self, player):
        if player == "player1":
            self.score1 += 1
        else:
            self.score2 += 1

    def draw_rect(self, color, rect):
        pygame.draw.rect(self.screen, color, rect)

    def draw_ellipse(self, color, rect):
        pygame.draw.ellipse(self.screen, color, rect)


    def update_board(self):
        # Update the display
        pygame.display.flip()
        # Control frame rate (60 FPS)
        self.clock.tick(60)

    def quit(self):
        # Quit Pygame
        pygame.quit()
