from ui.game_screen import GameScreen
from service.game import Game

if __name__ == '__main__':
    screen = GameScreen()
    screen.wait_for_start()
    use_ai = screen.use_ai()

    game = Game(use_ai=use_ai, game_screen=screen)
    game.play()
