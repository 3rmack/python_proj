import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return math.hypot(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "Point({0.x!r}, {0.y!r})".format(self)

    def __str__(self):
        return "({0.x!r}, {0.y!r})".format(self)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return Point(self.x, self.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return Point(self.x, self.y)

    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)

    def __imul__(self, other):
        self.x *= other.x
        self.y *= other.y
        return Point(self.x, self.y)

    def __truediv__(self, other):
        return Point(self.x / other.x, self.y / other.y)

    def __itruediv__(self, other):
        self.x /= other.x
        self.y /= other.y
        return Point(self.x, self.y)

    def __floordiv__(self, other):
        return Point(self.x // other.x, self.y // other.y)

    def __ifloordiv__(self, other):
        self.x //= other.x
        self.y //= other.y
        return Point(self.x, self.y)

q = Point(6, 1)
r = Point(2, 4)

p = q + r
print(p)

p += q
print(p)

p2 = q - r
print(p2)

p2 -= r
print(p2)

p = q * r
print(p)

p *= r
print(p)

p3 = q / r
print(p3)

p3 /= r
print(p3)

p4 = q//r
print(p4)

p4 //= r
print(p4)
# print(a == b)
# print(a.distance_from_origin(), a.x, a.y)
# a.x = 5
# a.y = 7
# print(a == b)
# print(a.distance_from_origin(), a.x, a.y)
# print(repr(a))
# print(str(a))


# class Circle(Point):
#     def __init__(self, radius, x=0, y=0):
#         super.__init__(x, y)
#         self.radius = radius
#
#     def edge_distance_from_origin(self):
#         return abs(self.distance_from_origin() - self.radius)
#
#     def area(self):
#         return math.pi * (self.radius ** 2)
#
#     def circumference(self):
#         return 2 * math.pi * self.radius
#
#     def __eq__(self, other):
#         return self.radius == other.radius and super.__eq__(other)
#
#     def __repr__(self):
#         return "Circle({0.radius!r}, {0.xir}, {0.y!r})".format(self)
#
#     def __str__(self):
#         return repr(self)
#
