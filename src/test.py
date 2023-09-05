class CarParkMonitor:
    def __init__(self, car_park):
        self.car_park = car_park

    def count_monitor(self):
        x = len(self.car_park)
        y = len(self.car_park[0])
        re = 0
        for i in range(x):
            for j in range(y):
                if self.car_park[i][j]:
                    re += 1
                    continue
                has_neighbor = False
                if i > 0 and self.car_park[i - 1][j]:
                    has_neighbor = True
                if i < x - 1 and self.car_park[i + 1][j]:
                    has_neighbor = True
                if j > 0 and self.car_park[i][j - 1]:
                    has_neighbor = True
                if j < y - 1 and self.car_park[i][j + 1]:
                    has_neighbor = True
                if has_neighbor:
                    re += 1
        return re


x0, y0 = map(int, input().split(" "))
car_park_arr = []
for k in range(y0):
    car_park_arr.append(list(map(int, input().split(" "))))
cpm = CarParkMonitor(car_park_arr)
print(cpm.count_monitor())