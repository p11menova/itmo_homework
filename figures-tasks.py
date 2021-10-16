from itmo_homework.Figures import *


def segment_lenght():
    with open('INPUT.TXT', encoding='utf-8') as f:
        data = f.read().split()
        point1 = Point(x=data[0], y=data[1])
        l = point1.find_distanse(int(data[2]), int(data[3]))
    with open('OUTPUT.TXT', mode='w', encoding='utf-8')as f1:
        print(round(l, 5), file=f1)


def triangle_square():
    with open('INPUT.TXT', encoding='utf-8') as f:
        data = list(map(lambda x: int(x), f.read().split()))
        iteration = iter(data)
        tr = Triangle(point1=Point(next(iteration), next(iteration)),
                      point2=Point(next(iteration), next(iteration)),
                      point3=Point(next(iteration), next(iteration)))

        s = tr.find_square(p=tr.find_perimeter()/2)
        with open('OUTPUT.TXT', mode='w', encoding='utf-8')as f1:
            print(round(s, 5), file=f1)


def two_circles():
    with open('INPUT.TXT', encoding='utf-8') as f:
        data = f.readlines()
        c1_info = list(map(lambda x: int(x),  data[0].split()))
        c1 = Circle(center_point=Point(c1_info[0], c1_info[1]), R=c1_info[2])

        c2_info = list(map(lambda x: int(x),  data[1].split()))
        answer = 'YES' if c1.is_intersection(center=Point(c2_info[0], c2_info[1]), r=c2_info[2]) else 'NO'
    with open('OUTPUT.TXT', mode='w', encoding='utf-8')as f1:
        print(answer, file=f1)



def meter():
    with open('INPUT.TXT', encoding='utf-8') as f:
        n = int(f.read(1))
        data = list(map(lambda x: int(x), f.read().split()))
        POINTS = []
        DISTANSES = []
        iteration = iter(data)
        for i in range(n):
            point = Point(x=next(iteration), y=next(iteration))
            POINTS.append(point)
        for j in range(n-1):
            DISTANSES.append(POINTS[0].find_distanse(POINTS[j+1].x, POINTS[j+1].y))

        with open('OUTPUT.TXT', mode='w', encoding='utf-8')as f1:
            print(len(set(DISTANSES)), file=f1)
            print('\n'.join([str(round(i, 12)) for i in sorted(list(set(DISTANSES)))]), file=f1)

