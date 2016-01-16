from unittest import TestCase
from vector import Vector

__author__ = 'caleb'


class TestVector(TestCase):
    def test_add(self):
        v1 = Vector([8.218, -9.341])
        v2 = Vector([-1.129, 2.111])

        self.assertEqual(v1.plus(v2), Vector([7.089, -7.229999999999999]))
        self.assertEqual(v2.plus(v1), Vector([7.089, -7.229999999999999]))

    def test_subtract(self):
        v1 = Vector([7.119, 8.215])
        v2 = Vector([-8.223, 0.878])

        self.assertEqual(v1.minus(v2), Vector([15.342, 7.337]))

    def test_scalar_multiplication_by_scalar(self):
        v = Vector([1.671, -1.012, -0.318])
        self.assertEqual(v.times_scalar(7.41), Vector([12.38211, -7.49892, -2.35638]))

    def test_magnitude(self):
        self.assertEquals(Vector([-0.221, 7.437]).magnitude(), 7.440282924728065)
        self.assertEquals(Vector([8.813, -1.331, -6.247]).magnitude(), 10.884187567292289)
