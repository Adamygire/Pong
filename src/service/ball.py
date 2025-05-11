import pygame
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, WHITE_COLOR


class Ball:
    size = 20
    center_x, center_y = (WINDOW_WIDTH // 2 - size // 2,
                          WINDOW_HEIGHT // 2 - size // 2)

    def __init__(self, screen):
        self.screen = screen
        self.dx = -4
        self.dy = -4
        self.rect = pygame.Rect(0, 0, Ball.size, Ball.size)
        self.recenter()

    def flip_horizontal(self):
        self.dx *= -1

    def flip_vertical(self):
        self.dy *= -1

    def handle_collision_with_vertical_edge(self):
        if self.rect.top <= 0 or self.rect.bottom >= WINDOW_HEIGHT:
            self.flip_vertical()

    def is_out_of_bounds(self, position=None):
        passed_left_wall = self.rect.left < 0
        passed_right_wall = self.rect.right > WINDOW_WIDTH
        if position == 'left':
            return passed_left_wall

        if position == 'right':
            return passed_right_wall

        print(f"passed_left_wall={passed_left_wall}; passed_right_wall={passed_right_wall}")
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
        glow_color = (255, 255, 255, 100)
        glow_surface = pygame.Surface(
            (self.rect.width + 20, self.rect.height + 20), pygame.SRCALPHA)
        pygame.draw.ellipse(glow_surface, glow_color, glow_surface.get_rect())
        self.screen.blit(glow_surface, (self.rect.x - 10, self.rect.y - 10))
        pygame.draw.ellipse(self.screen, WHITE_COLOR, self.rect)

    def has_collided(self, rect):
        return self.rect.colliderect(rect)
