from unittest import TestCase
from plane import Plane
from vector import Vector

__author__ = 'caleb'


class TestPlane(TestCase):
    def test_problems(self):
        """

        :type self: object
        """
        p1 = Plane(Vector([-0.412, 3.806, 0.728]), -3.46)
        p2 = Plane(Vector([1.03, -9.515, -1.82]), 8.65)
        self.assertEqual(p1, p2)

        p1 = Plane(Vector([2.611, 5.528, 0.283]), 4.6)
        p2 = Plane(Vector([7.715, 8.306, 5.342]), 3.76)
        self.assertFalse(p1.is_parallel_to(p2))


        p1 = Plane(Vector([-7.926, 8.625, -7.212]), -7.952)
        p2 = Plane(Vector([-2.642, 2.875, -2.404]), -2.443)
        self.assertNotEqual(p1, p2)
        self.assertTrue(p1.is_parallel_to(p2))


