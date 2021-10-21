from math import sqrt, pi


class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __copy__(self):
        return Point(self.x, self.y)

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __str__(self):
        return f'{self.x}, {self.y}'

    def find_distance(self, other) -> float:
        return isinstance(other, Point) and sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)


class Triangle:
    def __init__(self, point1: Point, point2: Point, point3: Point):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

        # стороны
        self.a = self.point1.find_distance(self.point2)
        self.b = self.point2.find_distance(self.point3)
        self.c = self.point3.find_distance(self.point1)

    def find_perimeter(self) -> float:
        return self.a + self.b + self.c

    def find_square(self, p) -> float:
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


class Circle:
    def __init__(self, center_point: Point, R):
        self.center_point = center_point
        self.ox = center_point.x
        self.oy = center_point.y
        self.R = R

    def find_lenght(self) -> float:
        return 2 * pi * self.R

    def find_square(self) -> float:
        return (self.R ** 2) * pi

    def is_inside_circle(self, point: Point) -> bool:
        return ((point.x - self.ox) ** 2 + (point.y - self.oy)) ** 2 <= self.R**2

    def is_intersection(self, center: Point, r):
        s = self.center_point.find_distance(center)
        return abs(self.R - r) < s < (self.R + r)

