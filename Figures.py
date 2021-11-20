from math import sqrt, pi


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __copy__(self):
        return Point(self.x, self.y)

    def __eq__(self, other) -> bool:
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __str__(self) -> str:
        return f'{self.x}, {self.y}'

    def __mul__(self, n: int):
        return Point(x=self.x * n, y=self.y * n)

    def find_distance(self, other) -> float:
        return isinstance(other, Point) and sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)


class Vector:
    def __init__(self, start_point: Point, finish_point: Point):
        self.s_point = start_point
        self.f_point = finish_point

    def __str__(self) -> str:
        return f'{str(self.s_point)} -> {str(self.f_point)}'

    def __copy__(self):
        return Vector(self.s_point, self.f_point)

    def __add__(self, other):
        if isinstance(other, Vector) and other.s_point == self.f_point:
            return Vector(start_point=self.s_point, finish_point=other.f_point)
        return 0

    def __sub__(self, other):
        if isinstance(other, Vector):
            other_vector = Vector(start_point=other.s_point,
                                 finish_point=Point(other.f_point.x * -1, other.f_point.y))
            return self + other_vector
        return 0

    def __mul__(self, n: int):
        return Vector(start_point=self.s_point * n, finish_point=self.f_point * n)

    def length(self) -> float:
        return sqrt((self.f_point.x - self.s_point.x) ** 2 + (self.f_point.y - self.s_point.y) ** 2)

    def scalar_mul(self, other, cosine) -> float:
        if isinstance(other, Vector):
            return self.length() * other.length() * cosine


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
    def __init__(self, center_point: Point, R: float):
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

    def is_intersection(self, center: Point, r: float):
        s = self.center_point.find_distance(center)
        return abs(self.R - r) < s < (self.R + r)

