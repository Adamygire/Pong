import pygame
from ..constants import WINDOW_WIDTH, WINDOW_HEIGHT, WHITE_COLOR


class Ball:
    size = 20
    center_x, center_y  = (WINDOW_WIDTH // 2 - size // 2, WINDOW_HEIGHT // 2 - size // 2)

    def __init__(self, screen):
        self.screen = screen
        self.dx = 2
        self.dy = 2
        self.rect = pygame.Rect(0, 0, Ball.size, Ball.size)
        self.recenter()

    def flip_horizontal(self):
        self.dx *= -1
        pygame.mixer.Sound("./sounds/bounce.mp3").play()

    def flip_vertical(self):
        self.dy *= -1
        pygame.mixer.Sound("./sounds/bounce.mp3").play()

    def handle_collision_with_vertical_edge(self):
        if self.rect.top <= 0 or self.rect.bottom >= WINDOW_HEIGHT:
            self.flip_vertical()

    def is_out_of_bounds(self, position='left'):
        passed_left_wall = self.rect.left < 0
        passed_right_wall = self.rect.right > WINDOW_WIDTH
        if position == 'left':
            return passed_left_wall

        if position == 'right':
            return passed_right_wall

        return passed_left_wall or passed_right_wall

    def set_location(self, location):
        self.rect.x, self.rect.y = location

    def recenter(self):
        self.rect.x = Ball.center_x
        self.rect.y = Ball.center_y

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

    def draw(self):
        pygame.draw.ellipse(self.screen, WHITE_COLOR, self.rect)

    def has_collided(self, rect):
        return self.rect.colliderect(rect)
