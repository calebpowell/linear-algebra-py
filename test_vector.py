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

    def test_normalization(self):
        normalized = Vector([5.581, -2.136]).normalized()
        self.assertEquals(normalized, Vector([0.9339352140866403, -0.35744232526233]))
        self.assertEquals(round(normalized.magnitude(), 1), 1)

        normalized = Vector([1.996, 3.108, -4.554]).normalized()
        self.assertEquals(normalized, Vector([0.3404012959433014, 0.5300437012984873, -0.7766470449528029]))
        self.assertEquals(round(normalized.magnitude(), 1), 1)

    def test_normalization_with_0_vector(self):
        self.assertRaises(Exception, Vector([0, 0]).normalized)

    def test_dot_product(self):
        v1 = Vector([7.887, 4.138])
        v2 = Vector([-8.802, 6.776])

        self.assertEqual(v1.dot_product(v2), -41.382286)
        self.assertEqual(v2.dot_product(v1), -41.382286)

        v1 = Vector([-5.955, -4.904, -1.874])
        v2 = Vector([-4.496, -8.755, 7.103])

        self.assertEqual(round(v1.dot_product(v2), 6), 56.397178)
        self.assertEqual(round(v2.dot_product(v1), 6), 56.397178)


