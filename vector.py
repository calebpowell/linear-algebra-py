import operator
import math
__author__ = 'caleb'


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
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
        new_coordinates = [c * x for x in self.coordinates]
        return Vector(new_coordinates)

    def magnitude(self):
        coordinates_squared = [x**2 for x in self.coordinates]
        return math.sqrt(sum(coordinates_squared))

    def normalized(self):
        try:
            return self.times_scalar(1/self.magnitude())
        except ZeroDivisionError:
            raise Exception('Cannot normalize the 0 vector')

    def dot_product(self, vector):
        new_coordinates = [x*y for x,y in zip(self.coordinates, vector.coordinates)]
        return sum(new_coordinates)

    def angle(self, vector):
        numerator = self.dot_product(vector)
        denominator = self.magnitude() * vector.magnitude()
        return math.acos((numerator/denominator))

    def angle_degrees(self, vector):
        return math.degrees(self.angle(vector))