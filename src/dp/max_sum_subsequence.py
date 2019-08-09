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


data = [16, 29, 0, -13, -15, -21, 3, 22, 2, -26]
print("Bruce result:", MaxSumSubSequence(data).bruce(), ",take time:",
      timeit.timeit("MaxSumSubSequence([16, 29, 0, -13, -15, -21, 3, 22, 2, -26]).bruce()", setup="from __main__ import MaxSumSubSequence", number=10000))
