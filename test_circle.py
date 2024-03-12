"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
from circle import Circle
import unittest
import math

# TODO write 3 tests as described above

class CircleTest(unittest.TestCase):
    """Tests for the Circle class"""
    def setUp(self):
        """create circles before each test"""
        self.circle_five = Circle(5)
        self.circle_ten = Circle(10)

    def test_add_area_positive(self):
        """add_area return a new circle whose area equal to the combined of two circles"""
        new_circle = self.circle_five.add_area(self.circle_ten)
        self.assertEqual(self.circle_five.get_area()+self.circle_ten.get_area(),
                         new_circle.get_area())
        self.assertEqual(math.hypot(self.circle_five.get_radius(),self.circle_ten.get_radius()),
                         new_circle.get_radius())
