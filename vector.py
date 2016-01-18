import operator
import math
from decimal import Decimal, getcontext
__author__ = 'caleb'

getcontext().prec = 30

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self, vector):
        new_coordinates = [x+y for x,y in zip(self.coordinates, vector.coordinates)]
        return Vector(new_coordinates)

    def minus(self, vector):
        new_coordinates = [x-y for x,y in zip(self.coordinates, vector.coordinates)]
        return Vector(new_coordinates)

    def times_scalar(self, c):
        new_coordinates = [Decimal(c) * x for x in self.coordinates]
        return Vector(new_coordinates)

    def magnitude(self):
        coordinates_squared = [x**Decimal(2) for x in self.coordinates]
        return sum(coordinates_squared).sqrt(getcontext())

    def normalized(self):
        try:
            return self.times_scalar(Decimal('1.0')/Decimal(self.magnitude()))
        except ZeroDivisionError:
            raise Exception('Cannot normalize the 0 vector')

    def dot(self, vector):
        new_coordinates = [x*y for x,y in zip(self.coordinates, vector.coordinates)]
        return sum(new_coordinates)

    def angle(self, vector):
        numerator = self.dot(vector)
        denominator = self.magnitude() * vector.magnitude()
        quotient = (numerator / denominator)
        return math.acos(quotient)

    def angle_degrees(self, vector):
        return math.degrees(self.angle(vector))

    def orthogonal(self, vector, tolerance=1e-10):
        return abs(self.dot(vector)) < tolerance

    def parallel(self, vector):
        return (self.is_zero()
                or vector.is_zero()
                or self.angle(vector) == 0
                or self.angle(vector) == math.pi)

    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance

    def projection_of(self, v):
        b_normalized = self.normalized()
        return b_normalized.times_scalar(v.dot(b_normalized))

    def orthog_comp(self, vector):
        return self.projection_of(vector).times_scalar(-1).plus(vector)