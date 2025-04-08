import pygame
from ..constants import WINDOW_WIDTH, WINDOW_HEIGHT, WHITE_COLOR


class Paddle:
    def __init__(self, screen, position='left'):
        width = 20
        height = 100
        self.screen = screen

        if position == 'left':
            location = 50
            self.up_key = pygame.K_w
            self.down_key = pygame.K_s
        else:
            location = WINDOW_WIDTH - 50 - width
            self.up_key = pygame.K_UP
            self.down_key = pygame.K_DOWN

        self.rect = pygame.Rect(location, WINDOW_HEIGHT //
                                2 - height // 2, width, height)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[self.up_key] and self.rect.top > 0:
            self.rect.y -= 20
        if keys[self.down_key] and self.rect.bottom < WINDOW_HEIGHT:
            self.rect.y += 20

    def draw(self):
        pygame.draw.rect(self.screen, WHITE_COLOR, self.rect)
