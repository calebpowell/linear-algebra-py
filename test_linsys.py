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

    def test_compute_triangular_form(self):
        p1 = Plane(normal_vector=Vector(['0','1','1']), constant_term='1')
        p2 = Plane(normal_vector=Vector(['0','0','1']), constant_term='2')
        p3 = Plane(normal_vector=Vector(['1','1','1']), constant_term='2')
        s = LinearSystem([p1, p2, p3])
        t = s.compute_triangular_form()

        self.assertEqual(t[0], p3, str(t[0]))
        self.assertEqual(t[1], p1, str(t[1]))
        self.assertEqual(t[2], p2, str(t[2]))

        p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
        p2 = Plane(normal_vector=Vector(['0','1','1']), constant_term='2')
        s = LinearSystem([p1,p2])
        t = s.compute_triangular_form()

        self.assertEqual(t[0], p1)
        self.assertEqual(t[1], p2)

        p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
        p2 = Plane(normal_vector=Vector(['1','1','1']), constant_term='2')
        s = LinearSystem([p1,p2])
        t = s.compute_triangular_form()

        self.assertEqual(t[0], p1, t)
        self.assertEqual(t[1], Plane(constant_term='1'), str(t[1]))

        p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
        p2 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
        p3 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
        p4 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')
        s = LinearSystem([p1,p2,p3,p4])
        t = s.compute_triangular_form()

        self.assertEqual(t[0], p1)
        self.assertEqual(t[1], Plane(normal_vector=Vector(['0','-1','-3']), constant_term='1'))
        self.assertEqual(t[2], Plane(normal_vector=Vector(['0','0','-3']), constant_term='3'))
        self.assertEqual(t[3], Plane())

        p1 = Plane(normal_vector=Vector(['0','1','1']), constant_term='1')
        p2 = Plane(normal_vector=Vector(['1','-1','1']), constant_term='2')
        p3 = Plane(normal_vector=Vector(['1','2','-5']), constant_term='3')
        s = LinearSystem([p1,p2,p3])
        t = s.compute_triangular_form()

        print t
        self.assertEqual(t[0], Plane(normal_vector=Vector(['1','-1','1']), constant_term='2'))
        self.assertEqual(t[1], Plane(normal_vector=Vector(['0','1','1']), constant_term='1'))
        self.assertEqual(t[2], Plane(normal_vector=Vector(['0','0','-9']), constant_term='-1'))

# if not (t[0] == Plane(normal_vector=Vector(['1','-1','1']), constant_term='2') and
#         t[1] == Plane(normal_vector=Vector(['0','1','1']), constant_term='1') and
#         t[2] == Plane(normal_vector=Vector(['0','0','-9']), constant_term='-2')):
#     print 'test case 4 failed'

    def test_triangular(self):
        p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
        p2 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
        p3 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
        s = LinearSystem([p1,p2,p3])

        self.assertFalse(s.triangular())

        p1 = Plane(normal_vector=Vector(['0','0','0']), constant_term='1')
        p2 = Plane(normal_vector=Vector(['1','1','1']), constant_term='2')
        s = LinearSystem([p1,p2])

        self.assertFalse(s.triangular())

        p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
        p2 = Plane(normal_vector=Vector(['0','1','1']), constant_term='2')
        p3 = Plane(normal_vector=Vector(['0','0','1']), constant_term='3')
        p4 = Plane(normal_vector=Vector(['0','0','0']), constant_term='0')
        s = LinearSystem([p1,p2,p3,p4])

        self.assertTrue(s.triangular())

        p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
        p2 = Plane(normal_vector=Vector(['0','1','1']), constant_term='2')
        p3 = Plane(normal_vector=Vector(['0','0','-1']), constant_term='3')
        s = LinearSystem([p1,p2,p3])

        self.assertTrue(s.triangular())