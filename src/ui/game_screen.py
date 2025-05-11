import pygame
import pygame_gui
from user_auth import validate_login, create_account
from constants import WHITE_COLOR, BLACK_COLOR, WINDOW_WIDTH, WINDOW_HEIGHT


class GameScreen:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Pong")
        self.font = pygame.font.SysFont("Courier", 24)
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.manager = pygame_gui.UIManager(
            (WINDOW_WIDTH, WINDOW_HEIGHT), "theme.json")
        self.clock = pygame.time.Clock()
        self.selected_mode = 'Player vs Player'

        # Login Elements
        self.username_input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(
                (WINDOW_WIDTH // 2 - 100, 150), (200, 30)),
            manager=self.manager
        )
        self.password_input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(
                (WINDOW_WIDTH // 2 - 100, 200), (200, 30)),
            manager=self.manager
        )
        self.password_input.set_text_hidden(True)

        self.login_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (WINDOW_WIDTH // 2 - 75, 250), (150, 40)),
            text='Log In',
            manager=self.manager
        )

        self.login_message = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(
                (WINDOW_WIDTH // 2 - 150, 100), (300, 30)),
            text='Welcome',
            manager=self.manager,
            object_id="#login_message"
        )

        self.start_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (WINDOW_WIDTH // 2 - 75, 410), (150, 50)),
            text='Start Game',
            manager=self.manager,
            visible=0
        )

        # AI Toggle Buttons
        self.ai_radio_ai = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (WINDOW_WIDTH // 2 - 75, 320), (150, 30)),
            text='Play vs AI',
            manager=self.manager
        )

        self.ai_radio_pvp = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (WINDOW_WIDTH // 2 - 75, 360), (150, 30)),
            text='Player vs Player',
            manager=self.manager
        )

    def show_game_over_screen(self, winner):
        label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(
                (WINDOW_WIDTH // 2 - 150, 50), (300, 50)),
            text=f"{winner} wins!",
            manager=self.manager
        )

        restart_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (WINDOW_WIDTH // 2 - 75, 250), (150, 50)),
            text="Restart",
            manager=self.manager
        )

        exit_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (WINDOW_WIDTH // 2 - 75, 320), (150, 50)),
            text="Exit",
            manager=self.manager
        )

        waiting = True
        while waiting:
            time_delta = self.clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == restart_button:
                            waiting = False
                        elif event.ui_element == exit_button:
                            pygame.quit()
                            exit()

                self.manager.process_events(event)

            self.manager.update(time_delta)
            self.screen.fill(BLACK_COLOR)
            self.manager.draw_ui(self.screen)
            pygame.display.update()

        label.kill()
        restart_button.kill()
        exit_button.kill()

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
                            username = self.username_input.get_text().strip()
                            password = self.password_input.get_text().strip()

                            if validate_login(username, password):
                                logged_in = True
                                self.login_message.set_text(
                                    "Login successful!")
                                self.start_button.show()
                            else:
                                created = create_account(username, password)
                                if created:
                                    logged_in = True
                                    self.login_message.set_text(
                                        "New account created!")
                                    self.start_button.show()
                                else:
                                    self.login_message.set_text(
                                        "Incorrect password for existing user.")

                        elif event.ui_element == self.ai_radio_ai:
                            self.selected_mode = 'Player vs AI'
                        elif event.ui_element == self.ai_radio_pvp:
                            self.selected_mode = 'Player vs Player'

                        elif event.ui_element == self.start_button and logged_in:
                            print("Selected mode:", self.selected_mode)
                            waiting = False

                self.manager.process_events(event)
                self.manager.update(time_delta)

                self.screen.fill(BLACK_COLOR)
                self.manager.draw_ui(self.screen)

                if self.selected_mode == 'Player vs AI':
                    pygame.draw.rect(self.screen, (0, 150, 0),
                                     self.ai_radio_ai.rect, 3)
                else:
                    pygame.draw.rect(self.screen, (0, 150, 0),
                                     self.ai_radio_pvp.rect, 3)

                pygame.display.update()

    def use_ai(self):
        return self.selected_mode == 'Player vs AI'

    def clear_screen(self):
        self.screen.fill((10, 10, 30))

    def draw_scoreboard(self, score1, score2):
        score_text = self.font.render(
            f"Player 1: {score1}  Player 2: {score2}", True, WHITE_COLOR)
        self.screen.blit(score_text, (WINDOW_WIDTH // 2 -
                         score_text.get_width() // 2, 20))
