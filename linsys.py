__author__ = 'caleb'

from decimal import Decimal, getcontext
from copy import deepcopy

from vector import Vector
from plane import Plane

getcontext().prec = 30


class LinearSystem(object):
    ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG = 'All planes in the system should live in the same dimension'
    NO_SOLUTIONS_MSG = 'No solutions'
    INF_SOLUTIONS_MSG = 'Infinitely many solutions'

    def __init__(self, planes):
        try:
            d = planes[0].dimension
            for p in planes:
                assert p.dimension == d

            self.planes = planes
            self.dimension = d

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)

    def swap_rows(self, row1, row2):
        self[row1], self[row2] = self[row2], self[row1]

    def multiply_coefficient_and_row(self, coefficient, row):
        p = self[row]
        self[row] = Plane(p.normal_vector.times_scalar(coefficient), p.constant_term * coefficient)

    def add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_be_added_to):
        if coefficient != 0:
            p = self[row_to_add]
            p = Plane(p.normal_vector.times_scalar(coefficient), (p.constant_term * coefficient))
            q = self[row_to_be_added_to]
            self[row_to_be_added_to] = Plane(q.normal_vector.plus(p.normal_vector),
                                                    q.constant_term + p.constant_term)

    def indices_of_first_nonzero_terms_in_each_row(self):
        num_equations = len(self)
        num_variables = self.dimension

        indices = [-1] * num_equations

        for i, p in enumerate(self.planes):
            try:
                indices[i] = p.first_nonzero_index(p.normal_vector)
            except Exception as e:
                if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                    continue
                else:
                    raise e

        return indices

    def nonzero_indices(self):
        return self.indices_of_first_nonzero_terms_in_each_row()

    def triangular(self):
        idx = self.nonzero_indices()
        for i, p in enumerate(idx):
            if i > 0:
                if p > -1 and idx[i-1] < 0:
                    return False
                elif p > -1 and p <= idx[i-1]:
                    return False
        return True

    def compute_triangular_form(self):
        sys = deepcopy(self)

        while not sys.triangular():
            idx = sys.nonzero_indices()
            for i, p in enumerate(idx):
                if i > 0:
                    if p < idx[i-1]:
                        sys.swap_rows(i, i-1)
                        break
                    elif p == idx[i-1]:
                        a = sys[i - 1].normal_vector[idx[i - 1]]
                        b = sys[i].normal_vector[idx[i]]
                        print 'a:%i, b:%i' % (a, b)
                        x = (-1 * b)/a
                        print 'x:%i' % x
                        sys.add_multiple_times_row_to_row(x, i-1, i)
                        break

        #Add multiples of rows to rows underneath
        # print "before multiples => %s" % sys
        # idx = sys.indices_of_first_nonzero_terms_in_each_row()
        # for i, p in enumerate(idx):
        #     if (i < (len(idx) -1)) and (p == idx[i+1]):
        #         a = sys[i].normal_vector[p]
        #         b = sys[i + 1].normal_vector[idx[i+1]]
        #         print 'a:%i, b:%i' % (a, b)
        #         x = (-1 * b)/a
        #         print 'x:%i' % x
        #         sys.add_multiple_times_row_to_row(x, i, i+1)
        #         break

        return sys

    def __len__(self):
        return len(self.planes)

    def __getitem__(self, i):
        return self.planes[i]

    def __setitem__(self, i, x):
        try:
            assert x.dimension == self.dimension
            self.planes[i] = x

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)

    def __str__(self):
        ret = 'Linear System:\n'
        temp = ['Equation {}: {}'.format(i + 1, p) for i, p in enumerate(self.planes)]
        ret += '\n'.join(temp)
        return ret


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps

