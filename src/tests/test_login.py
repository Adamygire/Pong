import unittest
from ui.game_screen import GameScreen

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.screen = GameScreen()

    def test_valid_login_credentials(self):
        self.assertTrue(self.screen.is_valid_login("player", "pong"))

    def test_invalid_username(self):
        self.assertFalse(self.screen.is_valid_login("wrong_user", "pong"))

    def test_invalid_password(self):
        self.assertFalse(self.screen.is_valid_login("player", "wrong_pass"))

    def test_invalid_credentials(self):
        self.assertFalse(self.screen.is_valid_login("wrong", "wrong"))
