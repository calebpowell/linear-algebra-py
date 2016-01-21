from unittest import TestCase
from vector import Vector
from decimal import Decimal as dec

__author__ = 'caleb'


class TestVector(TestCase):
    def assertVecEqual(self, expected_coordinates, actual, round_val=None):
        if round_val:
            self.assertEqual(expected_coordinates,
                             [round(x, round_val) for x in actual.coordinates])
        else:
            self.assertEqual(
                [dec(x) for x in expected_coordinates],
                [x for x in actual.coordinates])

    def test_add(self):
        v = Vector([8.218, -9.341])
        w = Vector([-1.129, 2.111])

        self.assertVecEqual(['7.08899999999999996802557689080', '-7.22999999999999909405801190587'], v.plus(w))
        self.assertEqual(v.plus(w), w.plus(v), "Vector addition is commutative!")

    def test_subtract(self):
        v = Vector([7.119, 8.215])
        w = Vector([-8.223, 0.878])

        self.assertVecEqual(['15.3420000000000005258016244625', '7.33699999999999985522691758888'], v.minus(w))

    def test_scalar_multiplication_by_scalar(self):
        v = Vector([1.671, -1.012, -0.318])
        self.assertVecEqual(
            ['12.3821100000000005402078784300', '-7.49892000000000022279067479758', '-2.35638000000000008138822948922'],
            v.times_scalar(7.41))

    def test_magnitude(self):
        self.assertEquals(Vector([-0.221, 7.437]).magnitude(), dec('7.44028292472806467554916796252'))
        self.assertEquals(Vector([8.813, -1.331, -6.247]).magnitude(), dec('10.8841875672922877669084935690'))

    def test_normalization(self):
        n = Vector([5.581, -2.136]).normalized()
        self.assertVecEqual(['0.933935214086640320939539156655', '-0.357442325262329993472768036987'], n)
        self.assertEquals(round(n.magnitude(), 1), 1)

        n = Vector([1.996, 3.108, -4.554]).normalized()
        self.assertVecEqual(['0.340401295943301353446730853387', '0.530043701298487295114197490245',
                             '-0.776647044952802834802650679030'], n)
        self.assertEquals(round(n.magnitude(), 1), 1)

    def test_normalization_with_0_vector(self):
        self.assertRaises(Exception, Vector([0, 0]).normalized)

    def test_dot_product(self):
        v = Vector([7.887, 4.138])
        w = Vector([-8.802, 6.776])

        self.assertEqual(round(v.dot(w), 6), -41.382286)
        self.assertEqual(v.dot(w), w.dot(v), "Vector dot multiplication is commutative")

        v = Vector([-5.955, -4.904, -1.874])
        w = Vector([-4.496, -8.755, 7.103])

        self.assertEqual(round(v.dot(w), 6), 56.397178)
        self.assertEqual(v.dot(w), w.dot(v), "Vector dot multiplication is commutative")

    def test_angle_in_radians(self):
        v = Vector([3.183, -7.627])
        w = Vector([-2.668, 5.319])

        self.assertEqual(round(v.angle(w), 5), 3.07203)
        self.assertEqual(v.angle(w), w.angle(v))

    def test_angle_in_degrees(self):
        v = Vector([3.183, -7.627])
        w = Vector([-2.668, 5.319])

        self.assertEqual(round(v.angle_degrees(w), 2), 176.01)
        self.assertEqual(v.angle_degrees(w), w.angle_degrees(v))

        v = Vector([7.35, 0.221, 5.188])
        w = Vector([2.751, 8.259, 3.985])

        self.assertEqual(round(v.angle_degrees(w), 3), 60.276)
        self.assertEqual(v.angle_degrees(w), w.angle_degrees(v))

    def test_parallel(self):
        self.assertTrue(Vector([-7.579, -7.88]).parallel(Vector([22.737, 23.64])))
        self.assertFalse(Vector([-2.029, 9.97, 4.172]).parallel(Vector([-9.231, -6.639, -7.245])))
        self.assertFalse(Vector([-2.328, -7.284, -1.124]).parallel(Vector([-1.821, 1.072, -2.94])))
        self.assertTrue(Vector([2.118, 4.827]).parallel(Vector([0, 0])))

    def test_orthogonal(self):
        self.assertFalse(Vector([-7.579, -7.88]).orthogonal(Vector([22.737, 23.64])))
        self.assertFalse(Vector([-2.029, 9.97, 4.172]).orthogonal(Vector([-9.231, -6.639, -7.245])))
        self.assertFalse(Vector([-2.328, -7.284, -1.124]).orthogonal(Vector([-1.821, 1.072, -2.94])))
        self.assertTrue(Vector([2.118, 4.827]).orthogonal(Vector([0, 0])))

    def test_parallel_to(self):
        basis = Vector([0.825, 2.036])
        v = Vector([3.039, 1.879])
        self.assertVecEqual([1.083, 2.672], v.component_parallel_to(basis), 3)

        basis = Vector([6.404, -9.144, 2.759, 8.718])
        v = Vector([3.009, -6.172, 3.692, -2.51])
        self.assertVecEqual([1.969, -2.811, 0.848, 2.68], v.component_parallel_to(basis), 3)

    def test_orthogonal_component(self):
        basis = Vector([-2.155, -9.353, -9.473])
        v = Vector([-9.88, -3.264, -8.159])
        self.assertVecEqual([-8.35, 3.376, -1.434], v.component_orthogonal_to(basis), 3)
        self.assertEquals(basis.angle_degrees(v.component_orthogonal_to(basis)), 90)

        basis = Vector([6.404, -9.144, 2.759, 8.718])
        v = Vector([3.009, -6.172, 3.692, -2.51])
        self.assertVecEqual([1.04, -3.361, 2.844, -5.19], v.component_orthogonal_to(basis), 3)
        self.assertEquals(basis.angle_degrees(v.component_orthogonal_to(basis)), 90)
