from unittest import TestCase
from vector import Vector

__author__ = 'caleb'


class TestVector(TestCase):
    def test_add(self):
        v1 = Vector([8.218, -9.341])
        v2 = Vector([-1.129, 2.111])

        self.assertEqual(v1.plus(v2), Vector(['7.08899999999999996802557689080', '-7.22999999999999909405801190587']))
        self.assertEqual(v2.plus(v1), Vector(['7.08899999999999996802557689080', '-7.22999999999999909405801190587']))

    def test_subtract(self):
        v1 = Vector([7.119, 8.215])
        v2 = Vector([-8.223, 0.878])

        self.assertEqual(v1.minus(v2), Vector(['15.3420000000000005258016244625', '7.33699999999999985522691758888']))

    def test_scalar_multiplication_by_scalar(self):
        v = Vector([1.671, -1.012, -0.318])
        self.assertEqual(v.times_scalar(7.41),
                         Vector(['12.3821100000000005402078784300', '-7.49892000000000022279067479758',
                                 '-2.35638000000000008138822948922']), v.times_scalar(7.41))

    def test_magnitude(self):
        self.assertEquals(Vector([-0.221, 7.437]).magnitude(), 7.440282924728065)
        self.assertEquals(Vector([8.813, -1.331, -6.247]).magnitude(), 10.884187567292289)

    def test_normalization(self):
        normalized = Vector([5.581, -2.136]).normalized()
        self.assertEquals(normalized, Vector(['0.933935214086640295130539147343', '-0.357442325262329983594964055642']),
                          normalized)
        self.assertEquals(round(normalized.magnitude(), 1), 1)

        normalized = Vector([1.996, 3.108, -4.554]).normalized()
        self.assertEquals(normalized, Vector(['0.340401295943301353537171045562', '0.530043701298487295255023200306',
                                              '-0.776647044952802835008995686630']), normalized)
        self.assertEquals(round(normalized.magnitude(), 1), 1)

    def test_normalization_with_0_vector(self):
        self.assertRaises(Exception, Vector([0, 0]).normalized)

    def test_dot_product(self):
        v1 = Vector([7.887, 4.138])
        v2 = Vector([-8.802, 6.776])

        self.assertEqual(round(v1.dot(v2), 6), -41.382286)
        self.assertEqual(round(v2.dot(v1), 6), -41.382286)

        v1 = Vector([-5.955, -4.904, -1.874])
        v2 = Vector([-4.496, -8.755, 7.103])

        self.assertEqual(round(v1.dot(v2), 6), 56.397178)
        self.assertEqual(round(v2.dot(v1), 6), 56.397178)

    def test_angle_in_radians(self):
        v1 = Vector([3.183, -7.627])
        v2 = Vector([-2.668, 5.319])

        self.assertEqual(round(v1.angle(v2), 5), 3.07203)
        self.assertEqual(round(v2.angle(v1), 5), 3.07203)

    def test_angle_in_degrees(self):
        v1 = Vector([3.183, -7.627])
        v2 = Vector([-2.668, 5.319])

        self.assertEqual(round(v1.angle_degrees(v2), 2), 176.01)

        v1 = Vector([7.35, 0.221, 5.188])
        v2 = Vector([2.751, 8.259, 3.985])

        self.assertEqual(round(v1.angle_degrees(v2), 3), 60.276)
        self.assertEqual(round(v2.angle_degrees(v1), 3), 60.276)
