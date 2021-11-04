from itmo_homework.Figures import *


def segment_lenght():
    with open('INPUT.TXT', encoding='utf-8') as f:
        data = f.read().split()
        point1 = Point(x=data[0], y=data[1])
        l = point1.find_distance(Point(data[2], data[3]))
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


def triangle_n_point():
    def tr_n_p_write_into_file(answer):
        with open('OUTPUT.TXT', mode='w', encoding='utf-8') as f1:
            print(answer, file=f1)

    with open('INPUT.TXT', encoding='utf-8') as f:
        data = list(map(lambda x: int(x), f.read().split()))
        iteration = iter(data)
        trpoint1 = Point(next(iteration), next(iteration))
        trpoint2 = Point(next(iteration), next(iteration))
        trpoint3 = Point(next(iteration), next(iteration))
        point = Point(next(iteration), next(iteration))

        if point == trpoint1 or point == trpoint2 or point == trpoint3:
            tr_n_p_write_into_file('IN')
        else:
            TR = Triangle(point1=trpoint1, point2=trpoint2, point3=trpoint3)
            S = TR.find_square(TR.find_perimeter()/2)

            tr1 = Triangle(point1=trpoint1, point2=trpoint2, point3=point)
            s1 = tr1.find_square(tr1.find_perimeter()/2)

            tr2 = Triangle(point1=trpoint1, point2=point, point3=trpoint3)
            s2 = tr2.find_square(tr2.find_perimeter()/2)

            tr3 = Triangle(point1=point, point2=trpoint2, point3=trpoint3)
            s3 = tr3.find_square(tr3.find_perimeter()/2)

            answer = 'IN' if S == (int(s1) + int(s2) + int(s3)) else 'OUT'
            tr_n_p_write_into_file(answer)

def meter():
    with open('INPUT.TXT', encoding='utf-8') as f:
        n = int(f.read(1))
        data = list(map(lambda x: int(x), f.read().split()))

        POINTS = []
        DISTANCES = []

        iteration = iter(data)
        for i in range(n):
            point = Point(x=next(iteration), y=next(iteration))
            POINTS.append(point)
        for j in range(n-1):
            DISTANCES.append(POINTS[0].find_distance(POINTS[j+1]))

        with open('OUTPUT.TXT', mode='w', encoding='utf-8')as f1:
            print(len(set(DISTANCES)), file=f1)
            print('\n'.join([str(round(i, 12)) for i in sorted(list(set(DISTANCES)))]), file=f1)

def vectors():
    v = Vector(start_point=Point(0, 0), finish_point=Point(3, 3))
    v2 = Vector(start_point=Point(3, 3), finish_point=Point(2, 2))

    print(v + v2)
    print(v - v2)
    print(v * 4)
    print(v.scalar_mul(other=v2, cosine=1))

vectors()