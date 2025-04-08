import unittest
from service.paddle import Paddle

class TestPaddle(unittest.TestCase):
    def setUp(self):
        self.paddle = Paddle(None)

    def test_created_paddle_has_position_as_left(self):
        self.assertEqual(self.paddle.rect.x, 50)


    def test_created_paddle_can_be_right(self):
        self.assertNotEqual(Paddle(None, position="right").rect.x, 50)
