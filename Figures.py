from math import sqrt, pi


class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def make_copy(self):
        return self.x, self.y

    def find_distanse(self, x1: int, y1: int) -> float:
        return sqrt((x1 - self.x)**2 + (y1 - self.y)**2)


class Triangle:
    def __init__(self, point1: Point, point2: Point, point3: Point):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

        # стороны
        self.a = self.point1.find_distanse(self.point2.x, self.point2.y)
        self.b = self.point2.find_distanse(self.point3.x, self.point3.y)
        self.c = self.point3.find_distanse(self.point1.x, self.point1.y)

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

    def fing_lenght(self) -> float:
        return 2 * pi * self.R

    def find_square(self) -> float:
        return (self.R ** 2) * pi

    def is_inside_circle(self, point: Point) -> bool:
        return ((point.x - self.ox) ** 2 + (point.y - self.oy)) ** 2 <= self.R**2

    def is_intersection(self, center: Point, r):
        s = self.center_point.find_distanse(center.x, center.y)
        return abs(self.R - r) < s < (self.R + r)

