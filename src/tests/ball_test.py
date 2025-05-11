import unittest
from service.ball import Ball
from constants import WINDOW_HEIGHT


class TestBall(unittest.TestCase):
    def setUp(self):
        self.ball = Ball(None)

    def test_created_ball_has_center_as_location(self):
        self.assertEqual(self.ball.rect.x, Ball.center_x)
        self.assertEqual(self.ball.rect.y, Ball.center_y)

    def test_created_ball_is_not_out_of_bounds(self):
        self.assertFalse(self.ball.is_out_of_bounds())


    def test_ball_can_recenter(self):
        self.ball.set_location((100, 100))
        self.assertNotEqual(self.ball.rect.x, Ball.center_x)
        self.assertNotEqual(self.ball.rect.y, Ball.center_y)

        self.ball.recenter()
        self.assertEqual(self.ball.rect.x, Ball.center_x)
        self.assertEqual(self.ball.rect.y, Ball.center_y)


    def test_ball_moves_correctly(self):
        initial_pos = self.ball.rect.topleft
        self.ball.move()
        self.assertNotEqual(self.ball.rect.topleft, initial_pos)

    def test_ball_flips_horizontally(self):
        expected_dx = -self.ball.dx
        self.ball.flip_horizontal()
        self.assertEqual(self.ball.dx, expected_dx)

    def test_ball_flips_vertically(self):
        expected_dy = -self.ball.dy
        self.ball.handle_collision_with_vertical_edge()
        self.ball.flip_vertical()
        self.assertEqual(self.ball.dy, expected_dy)

    def test_ball_flips_vertically_when_hitting_top_wall(self):
        self.ball.dy = -1000
        expected_dy = -self.ball.dy
        self.ball.move()
        self.ball.handle_collision_with_vertical_edge()
        self.assertEqual(self.ball.dy, expected_dy)


    def test_ball_flips_vertically_when_hitting_bottom_wall(self):
        self.ball.dy = 1000
        expected_dy = -self.ball.dy
        self.ball.move()
        self.ball.handle_collision_with_vertical_edge()
        self.assertEqual(self.ball.dy, expected_dy)


    def test_ball_is_out_of_bounds_left(self):
        self.ball.dx = -1000
        self.assertFalse(self.ball.is_out_of_bounds(position="left"))
        self.ball.move()
        self.assertFalse(self.ball.is_out_of_bounds(position="right"))
        self.assertTrue(self.ball.is_out_of_bounds(position="left"))
        self.assertTrue(self.ball.is_out_of_bounds())


    def test_ball_is_out_of_bounds_right(self):
        self.assertFalse(self.ball.is_out_of_bounds(position="right"))
        self.ball.dx = 1000
        self.ball.move()
        self.assertFalse(self.ball.is_out_of_bounds(position="left"))
        self.assertTrue(self.ball.is_out_of_bounds(position="right"))
        self.assertTrue(self.ball.is_out_of_bounds())
