class RoadLightning:
    def __init__(self, _arr):
        self.n = len(_arr)
        tuple_arr = [(max(0, 100 * i - _arr[i]), min(100 * (self.n - 1), 100 * i + _arr[i])) for i in range(self.n)]
        # 需要根据区间左节点排序
        tuple_arr.sort(key=lambda x: x[0])
        start, end = tuple_arr[0]
        self.lights = []
        for i in range(1, self.n):
            left, right = tuple_arr[i]
            # 与上个区间无交集（如果不对区间左节点排序，则这里可能会忽略下个区间与上个区间有交集的情况，会重复计算）
            if left > end:
                self.lights.append((start, end))
                start, end = left, right
            # 与上个区间有交集
            else:
                start = min(start, left)
                end = max(end, right)
        self.lights.append((start, end))

    @staticmethod
    def create_from_console():
        _ = input()
        return RoadLightning(list(map(int, input().split())))

    def count_shadow(self):
        return 100 * (self.n - 1) - sum(light[1] - light[0] for light in self.lights)

assert RoadLightning([50, 50]).count_shadow() == 0
assert RoadLightning([50, 70, 20, 70]).count_shadow() == 20
assert RoadLightning([10, 10, 10, 10, 10, 10, 10, 10]).count_shadow() == 560
assert RoadLightning([10, 10, 10, 250, 10, 10, 10, 10]).count_shadow() == 160