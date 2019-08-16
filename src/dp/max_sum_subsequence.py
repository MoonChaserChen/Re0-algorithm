import timeit


class MaxSumSubSequence:
    def __init__(self, arr):
        self.arr = arr

    # 暴力解法
    def bruce(self):
        le = len(self.arr)
        max_result = None
        for i in range(le):
            for j in range(i + 1):
                max_result = max(max_result, sum(self.arr[j:i + 1])) if max_result else sum(self.arr[j:i + 1])
        return max_result

    # 递归
    def ite(self):
        # 以index为ix结尾的连续子序列最大和
        def ite_step(ix):
            if ix == 0:
                return self.arr[ix]
            return self.arr[ix] if ite_step(ix - 1) <= 0 else self.arr[ix] + ite_step(ix - 1)

        le = len(self.arr)
        return max(ite_step(i) for i in range(le))


data = [16, 29, 0, -13, -15, -21, 3, 22, 2, -26]
mss = MaxSumSubSequence(data)
print("Bruce result:", mss.bruce(), ", take time:", timeit.timeit("MaxSumSubSequence([16, 29, 0, -13, -15, -21, 3, 22, 2, -26]).bruce()", setup="from __main__ import MaxSumSubSequence", number=10000))
print("Bruce result:", mss.ite(), ", take time:", timeit.timeit("MaxSumSubSequence([16, 29, 0, -13, -15, -21, 3, 22, 2, -26]).ite()", setup="from __main__ import MaxSumSubSequence", number=10000))
