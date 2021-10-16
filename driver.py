from typing import List


class Driver:
    def __init__(self, name: str, time_for_one: List[int], full_time: int):
        self.name = name
        self.time_for_one = time_for_one
        self.full_time = full_time

    def for_sorting(self):
        return self.name, self.full_time


with open('INPUT.TXT', encoding='utf-8') as f1:
    data = f1.readlines()
    n, m = int(data[0][0]), int(data[0][2])

DRIVERS = []
for i in range(1, 2*n+1, 2):
    time_for_circle = list(map(lambda x: int(x), data[i+1].split()))
    dr = Driver(data[i], time_for_circle, full_time=sum(time_for_circle))
    DRIVERS.append(dr)


winner = sorted(DRIVERS, key=lambda x: x.for_sorting()[1])[0].name
with open('OUTPUT.txt', mode='w', encoding='utf-8') as f2:
    print(winner, file=f2)
