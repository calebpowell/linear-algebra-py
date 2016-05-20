from unittest import TestCase
from plane import Plane
from vector import Vector
from linsys import LinearSystem
from decimal import Decimal

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
        self.assertEqual(t[1], p2)
        self.assertEqual(t[2], Plane(normal_vector=Vector(['0','0','-2']), constant_term='2'))
        self.assertEqual(t[3], Plane())

        p1 = Plane(normal_vector=Vector(['0','1','1']), constant_term='1')
        p2 = Plane(normal_vector=Vector(['1','-1','1']), constant_term='2')
        p3 = Plane(normal_vector=Vector(['1','2','-5']), constant_term='3')
        s = LinearSystem([p1,p2,p3])
        t = s.compute_triangular_form()

        self.assertEqual(t[0], Plane(normal_vector=Vector(['1','-1','1']), constant_term='2'))
        self.assertEqual(t[1], Plane(normal_vector=Vector(['0','1','1']), constant_term='1'))
        self.assertEqual(t[2], Plane(normal_vector=Vector(['0','0','-9']), constant_term='-2'))

    def test_compute_rref(self):

        p1 = Plane(normal_vector=Vector(['2','1','1']), constant_term='1')
        p2 = Plane(normal_vector=Vector(['0','3','3']), constant_term='3')
        p3 = Plane(normal_vector=Vector(['0','0','1']), constant_term='1')
        r = LinearSystem([p1, p2, p3]).compute_rref()

        self.assertEqual(r[0], Plane(normal_vector=Vector(['1','0','0']), constant_term='0'), str(r[0]))
        self.assertEqual(r[1], Plane(normal_vector=Vector(['0','1','0']), constant_term='0'), str(r[1]))
        self.assertEqual(r[2], p3, str(r[2]))

        p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
        p2 = Plane(normal_vector=Vector(['0','1','1']), constant_term='2')
        r = LinearSystem([p1, p2]).compute_rref()

        self.assertEqual(r[0], Plane(normal_vector=Vector(['1','0','0']), constant_term='-1'), str(r[0]))
        self.assertEqual(r[1], p2)

        p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
        p2 = Plane(normal_vector=Vector(['1','1','1']), constant_term='2')
        r = LinearSystem([p1, p2]).compute_rref()

        self.assertEqual(r[0], p1)
        self.assertEqual(r[1], Plane(constant_term='1'))

        p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
        p2 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
        p3 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
        p4 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')
        r = LinearSystem([p1, p2, p3, p4]).compute_rref()

        self.assertEqual(r[0], Plane(normal_vector=Vector(['1','0','0']), constant_term='0'))
        self.assertEqual(r[1], p2)
        self.assertEqual(r[2], Plane(normal_vector=Vector(['0','0','-2']), constant_term='2'))
        self.assertEqual(r[3], Plane())

        p1 = Plane(normal_vector=Vector(['0','1','1']), constant_term='1')
        p2 = Plane(normal_vector=Vector(['1','-1','1']), constant_term='2')
        p3 = Plane(normal_vector=Vector(['1','2','-5']), constant_term='3')
        r = LinearSystem([p1, p2, p3]).compute_rref()

        self.assertEqual(r[0], Plane(normal_vector=Vector(['1','0','0']), constant_term=Decimal('23')/Decimal('9')))
        self.assertEqual(r[1], Plane(normal_vector=Vector(['0','1','0']), constant_term=Decimal('7')/Decimal('9')))
        self.assertEqual(r[2], Plane(normal_vector=Vector(['0','0','1']), constant_term=Decimal('2')/Decimal('9')))
