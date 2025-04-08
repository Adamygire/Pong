import unittest
from ..service.ball import Ball

class TestBall(unittest.TestCase):
    def setUp(self):
        self.ball = Ball(None)

    def test_created_ball_has_center_as_location(self):
        self.assertEqual(self.ball.rect.x, Ball.center_x)
        self.assertEqual(self.ball.rect.y, Ball.center_y)

    def test_created_ball_is_not_out_of_bounds(self):
        self.assertFalse(self.ball.is_out_of_bounds())
