from itmo_homework.Figures import Vector, Point


class Vehicle:
    def __init__(self, direction: Vector):
        self.direction = direction
        self.start, self.finish = direction.s_point, direction.f_point

        self.speed = self.direction.length()
        self.writing = True
        self.written_route = []

    def move(self, n):
        ans = input('записывать данное перемещение? (yes/no):')
        self.writing = True if ans == 'yes' else False

        self.start = self.direction.s_point
        self.direction = self.direction * n
        self.finish = self.direction.f_point
        # if start.find_distance(finish)
        if self.writing:
            self.written_route.append(f'from {self.start} to {self.finish};'
                                      f' distance = {self.direction.length()}')

    def get_written_route(self):
        return '\n'.join(self.written_route)


# v = Vehicle(Vector(Point(0, 0), Point(5, 0)))
# v.move(4)
# v.move(5)
# print(v.get_written_route())


class Car(Vehicle):
    def __init__(self, direction: Vector, petrol: int):
        super().__init__(direction)
        self.__petrol = petrol


    @property
    def petrol(self):
        return self.__petrol

    @petrol.setter
    def petrol(self, petrol_add: int):
        self.__petrol += petrol_add

    def move(self, n):
        if n * self.speed <= self.__petrol:
            super().move(n)
            self.__petrol -= n * self.speed
        else:
            print('перемещение невозможно: не хватает бензина!')


c = Car(Vector(Point(0, 0), Point(7, 7)), petrol=30)
c.move(3)
c.move(1)
print(c.get_written_route())
