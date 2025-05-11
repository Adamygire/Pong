import pygame
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, WHITE_COLOR
import random


class Paddle:
    def __init__(self, screen, position='left', is_ai=False, ball=None):
        width = 20
        height = 100
        self.screen = screen
        self.is_ai = is_ai
        self.ball = ball

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
        self.speed = 12

    def move(self):
        if self.is_ai and self.ball:
            if self.ball.rect.centery > self.rect.centery and self.rect.bottom < WINDOW_HEIGHT:
                self.rect.y += 6
            elif self.ball.rect.centery < self.rect.centery and self.rect.top > 0:
                self.rect.y -= 6
        else:
            keys = pygame.key.get_pressed()
            if keys[self.up_key] and self.rect.top > 0:
                self.rect.y -= 10
            if keys[self.down_key] and self.rect.bottom < WINDOW_HEIGHT:
                self.rect.y += 10

    def move_player(self):
        keys = pygame.key.get_pressed()
        if keys[self.up_key] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[self.down_key] and self.rect.bottom < WINDOW_HEIGHT:
            self.rect.y += self.speed

    def move_ai(self):
        offset = random.randint(-15, 15)
        if abs(self.ball.rect.centery - self.rect.centery) > 30:
            if self.ball.rect.centery + offset < self.rect.centery and self.rect.top > 0:
                self.rect.y -= self.speed
            elif self.ball.rect.centery + offset > self.rect.centery and self.rect.bottom < WINDOW_HEIGHT:
                self.rect.y += self.speed

    def draw(self):
        pygame.draw.rect(self.screen, WHITE_COLOR, self.rect)
