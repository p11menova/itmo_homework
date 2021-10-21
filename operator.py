from itmo_homework. models_for_operator import *
OPERATORS = dict()


def circle_n_point(circle: Circle, point: Point):
    return True if circle.center_point.find_distance(point) <= circle.R else False


def main():
    for i in range(int(input())):
        name = input()
        x, y, r = map(int, input().split())
        if name in OPERATORS.keys():
            OPERATORS[name].append(Circle(center_point=Point(x, y), R=r))
        else:
            OPERATORS[name] = [Circle(center_point=Point(x, y), R=r)]

    xa, ya = map(int, input().split())
    user_point = Point(xa, ya)
    for k in OPERATORS.keys():
        answer = len(list(filter(lambda x: circle_n_point(circle=x, point=user_point), OPERATORS[k])))

        print(k, answer)

main()