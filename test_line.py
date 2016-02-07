from unittest import TestCase
from line import Line
from vector import Vector
from decimal import Decimal as dec

__author__ = 'caleb'


class TestLine(TestCase):
    def test_parallel(self):
        l1 = Line(Vector([3, -2]), 1)
        l2 = Line(Vector([-6, 4]), 0)
        self.assertTrue(l1.is_parallel_to(l2))

        l1 = Line(Vector([3, -2]), 8)
        l2 = Line(Vector([-6, 4]), 10)
        self.assertTrue(l1.is_parallel_to(l2))

        l1 = Line(Vector([1, 2]), 3)
        l2 = Line(Vector([1, -1]), 2)
        self.assertFalse(l1.is_parallel_to(l2))
        l1 = Line(Vector([1, 2]), 13)
        l2 = Line(Vector([1, -1]), 12)
        self.assertFalse(l1.is_parallel_to(l2))

    def test_coincident(self):
        l1 = Line(Vector([3, -2]), 1)
        l2 = Line(Vector([3, -2]), 1)
        self.assertEquals(l1, l2)

        l1 = Line(Vector([2, 3]), 6)
        l2 = Line(Vector([4, 6]), 12)
        self.assertEquals(l1, l2)

        l1 = Line(Vector([2, 3]), 6)
        l2 = Line(Vector([2, 3]), 12)
        self.assertNotEquals(l1, l2)

        l1 = Line(Vector([1, 2]), 3)
        l2 = Line(Vector([1, -1]), 2)
        self.assertNotEquals(l1, l2)

    def test_intersection(self):
        l1 = Line(Vector([1, 2]), 3)
        l2 = Line(Vector([1, -1]), 2)
        self.assertEquals(((dec(7)/dec(3)), (dec(1)/dec(3))), l1.intersection(l2).coordinates)
        self.assertEquals(((dec(7)/dec(3)), (dec(1)/dec(3))), l2.intersection(l1).coordinates)

    def test_problems(self):
        l1 = Line(Vector([4.046, 2.836]), 1.21)
        l2 = Line(Vector([10.115, 7.09]), 3.025)

        self.assertTrue(None == l1.intersection(l2))
        self.assertTrue(l1.__eq__(l2))

        l1 = Line(Vector([7.204, 3.182]), 8.68)
        l2 = Line(Vector([8.172, 4.114]), 9.883)

        self.assertEquals((dec('1.17277663546464155833736023125'), dec('0.0726955116633319428771277112348')),
                           l1.intersection(l2).coordinates)
        self.assertFalse(l1.__eq__(l2))

        l1 = Line(Vector([1.182, 5.562]), 6.744)
        l2 = Line(Vector([1.773, 8.343]), 9.525)

        self.assertEquals(None, l1.intersection(l2))
        self.assertFalse(l1.__eq__(l2))

