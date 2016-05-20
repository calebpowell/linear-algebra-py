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

    def contains_nonzero_coefficient_after(self, start, c_index):
        for i in range(start + 1, len(self)):
            if self[i].normal_vector[c_index] != 0:
                return i

        return None

    def compute_triangular_form(self):
        sys = deepcopy(self)

        m = len(sys)
        n = sys.dimension
        j = 0
        for i in range(0, m):
            while j < n:
                # consider the coefficient of var j in row i
                c = MyDecimal(sys[i].normal_vector[j])
                if c.is_near_zero():
                    # determine whether a row under i contains a non-zero coefficient for var j
                    idx = sys.contains_nonzero_coefficient_after(i, j)
                    if idx > i:
                        sys.swap_rows(i, idx)
                    else:
                        j += 1
                        continue

                # clear all terms with var j below row i
                for k in range(i+1, m):
                    if sys[k].normal_vector[j] != 0:
                        a = sys[i].normal_vector[j]
                        d = sys[k].normal_vector[j]
                        # consider:
                        # ax + by + cz = 1 (eq#1)
                        # dx + ey + fz = 2 (eq#2)
                        # to make x==0 in eq#2, we must make d==0:
                        # na + d = 0
                        # na = -d
                        # n = -d/a
                        coefficient = (-d)/a
                        sys.add_multiple_times_row_to_row(coefficient, i, k)

                j += 1
                break

        return sys

    def compute_rref(self):
        sys = self.compute_triangular_form()

        pivots = sys.indices_of_first_nonzero_terms_in_each_row()

        for i in range(0, len(sys)):
            if pivots[i] > -1 and sys[i].normal_vector[pivots[i]] != 1:
                x = sys[i].normal_vector[pivots[i]]
                sys.multiply_coefficient_and_row(1/x, i)

        for i in range(0, len(sys)):
            for j in range(i, sys.dimension):
                c = sys[i].normal_vector[j]
                if c != 0 and j in pivots and pivots.index(j) > i:
                    x = sys[pivots.index(j)].normal_vector[j]
                    sys.add_multiple_times_row_to_row(-c/x, pivots.index(j), i)



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

