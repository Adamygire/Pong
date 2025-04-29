import pygame
import pygame_gui
from constants import WHITE_COLOR, BLACK_COLOR, WINDOW_WIDTH, WINDOW_HEIGHT


class GameScreen:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Pong")
        self.font = pygame.font.SysFont("Courier", 24)
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.manager = pygame_gui.UIManager((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()

        # Login elements
        self.username_input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((WINDOW_WIDTH // 2 - 100, 150), (200, 30)),
            manager=self.manager
        )
        self.password_input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((WINDOW_WIDTH // 2 - 100, 200), (200, 30)),
            manager=self.manager
        )
        self.password_input.set_text_hidden(True)

        self.login_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((WINDOW_WIDTH // 2 - 75, 250), (150, 40)),
            text='Log In',
            manager=self.manager
        )

        self.login_message = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((WINDOW_WIDTH // 2 - 150, 300), (300, 30)),
            text='',
            manager=self.manager
        )

        # Start Game Button (initially hidden)
        self.start_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((WINDOW_WIDTH // 2 - 75, 350), (150, 50)),
            text='Start Game',
            manager=self.manager,
            visible=0
        )

    def wait_for_start(self):
        waiting = True
        logged_in = False

        while waiting:
            time_delta = self.clock.tick(60) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.login_button and not logged_in:
                            username = self.username_input.get_text()
                            password = self.password_input.get_text()

                            if username == "player" and password == "pong":
                                logged_in = True
                                self.login_message.set_text("Login successful!")
                                self.start_button.show()
                            else:
                                self.login_message.set_text("Invalid credentials. Try again.")

                        if event.ui_element == self.start_button and logged_in:
                            waiting = False

                self.manager.process_events(event)

            self.manager.update(time_delta)
            self.screen.fill(BLACK_COLOR)
            self.manager.draw_ui(self.screen)
            pygame.display.update()

    def clear_screen(self):
        self.screen.fill(BLACK_COLOR)

    def draw_scoreboard(self, score1, score2):
        score_text = self.font.render(
            f"Player 1: {score1}  Player 2: {score2}", True, WHITE_COLOR)
        self.screen.blit(score_text, (WINDOW_WIDTH // 2 - score_text.get_width() // 2, 20))
        
def is_valid_login(self, username, password):
    return username == "player" and password == "pong"