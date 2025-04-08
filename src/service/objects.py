import pygame
from constants import *


class Paddle:
    def __init__(self, position='left'):
        width = 20
        height = 100

        if position is 'left':
            location = 50
        else:
            location = WINDOW_WIDTH - 50 - width
        self.rect = pygame.Rect(location, WINDOW_HEIGHT //
                                2 - height // 2, width, height)


class Ball:
    size = BALL_SIZE

    def __init__(self):
        self.rect = pygame.Rect(0, 0, Ball.size, Ball.size)
        self.recenter()
        self.dx = 2
        self.dy = 2

    def flip_horizontal(self):
        self.dx *= -1
        pygame.mixer.Sound("./sounds/bounce.mp3").play()

    def flip_vertical(self):
        self.dy *= -1
        pygame.mixer.Sound("./sounds/bounce.mp3").play()

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
