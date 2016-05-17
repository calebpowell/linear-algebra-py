from unittest import TestCase
from plane import Plane
from vector import Vector
from linsys import LinearSystem

__author__ = 'caleb'


class TestLinearSystem(TestCase):

    def test_swap_rows(self):

        p0 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
        p1 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
        p2 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
        p3 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')

        s = LinearSystem([p0,p1,p2,p3])
        s.swap_rows(0,1)
        self.assertEqual(s[0], p1)
        self.assertEqual(s[1], p0)
        self.assertEqual(s[2], p2)
        self.assertEqual(s[3], p3)

        s.swap_rows(1,3)
        self.assertEqual(s[0], p1)
        self.assertEqual(s[1], p3)
        self.assertEqual(s[2], p2)
        self.assertEqual(s[3], p0)

        s.swap_rows(3,1)
        self.assertEqual(s[0], p1)
        self.assertEqual(s[1], p0)
        self.assertEqual(s[2], p2)
        self.assertEqual(s[3], p3)

        s.multiply_coefficient_and_row(1,0)
        self.assertEqual(s[0], p1)
        self.assertEqual(s[1], p0)
        self.assertEqual(s[2], p2)
        self.assertEqual(s[3], p3)

        s.multiply_coefficient_and_row(-1,2)
        self.assertEqual(s[0], p1)
        self.assertEqual(s[1], p0)
        self.assertEqual(s[2], Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3'))
        self.assertEqual(s[3], p3)

        s.multiply_coefficient_and_row(10,1)
        self.assertEqual(s[0], p1)
        self.assertEqual(s[1], Plane(normal_vector=Vector(['10','10','10']), constant_term='10'))
        self.assertEqual(s[2], Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3'))
        self.assertEqual(s[3], p3)


    def test_multiply_coefficient_and_rows(self):

        p0 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
        p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
        p2 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
        p3 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')

        s = LinearSystem([p0,p1,p2,p3])

        s.multiply_coefficient_and_row(1,0)
        self.assertEqual(s[0], p0)
        self.assertEqual(s[1], p1)
        self.assertEqual(s[2], p2)
        self.assertEqual(s[3], p3)

        s.multiply_coefficient_and_row(-1,2)
        self.assertEqual(s[0], p0)
        self.assertEqual(s[1], p1)
        self.assertEqual(s[2], Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3'))
        self.assertEqual(s[3], p3)

        s.multiply_coefficient_and_row(10,1)
        self.assertEqual(s[0], p0)
        self.assertEqual(s[1], Plane(normal_vector=Vector(['10','10','10']), constant_term='10'))
        self.assertEqual(s[2], Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3'))
        self.assertEqual(s[3], p3)

    def test_add_multiple_times_to_row(self):

        p0 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
        p1 = Plane(normal_vector=Vector(['10','10','10']), constant_term='10')
        p2 = Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3')
        p3 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')

        s = LinearSystem([p0,p1,p2,p3])

        s.add_multiple_times_row_to_row(0,0,1)
        self.assertEqual(s[0], p0)
        self.assertEqual(s[1], p1)
        self.assertEqual(s[2], p2)
        self.assertEqual(s[3], p3)

        s.add_multiple_times_row_to_row(1,0,1)
        self.assertEqual(s[0], p0)
        self.assertEqual(s[1], Plane(normal_vector=Vector(['10','11','10']), constant_term='12'), str(s[1]))
        self.assertEqual(s[2], p2)
        self.assertEqual(s[3], p3)

        s.add_multiple_times_row_to_row(-1,1,0)
        self.assertEqual(s[0], Plane(normal_vector=Vector(['-10','-10','-10']), constant_term='-10'), str(s[0]))
        self.assertEqual(s[1], Plane(normal_vector=Vector(['10','11','10']), constant_term='12'), str(s[1]))
        self.assertEqual(s[2], p2)
        self.assertEqual(s[3], p3)
