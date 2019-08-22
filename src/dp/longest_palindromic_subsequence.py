import timeit


class LongestPalindromicSubSequence:
    def __init__(self, arr):
        self.arr = arr

    @staticmethod
    def is_palindromic(arr):
        le = len(arr)
        for i in range(le // 2):
            if arr[i] != arr[le - 1 - i]:
                return False
        return True

    # 暴力解法
    def bruce(self):
        result = self.arr[0:1]
        max_length = 1
        le = len(self.arr)
        for i in range(le):
            for j in range(i + 1, le):
                temp = self.arr[i:j + 1]
                le_step = j + 1 - i
                if self.is_palindromic(temp) and le_step > max_length:
                    max_length = le_step
                    result = temp
        return result

    # 自底向上动态规划
    def dp(self):
        le = len(self.arr)
        dp = [([0] * le) for i in range(le)]
        result = self.arr[0:1]
        max_length = 1
        # i表示下标差值
        for i in range(le):
            # j, k表示起始下标，结束下标
            for j in range(le - i):
                k = i + j
                if self.arr[j] == self.arr[k] and (i < 3 or dp[j + 1][k - 1]):
                    dp[j][k] = 1
                    if i + 1 > max_length:
                        result = self.arr[j:k + 1]
        return result


data = ['d', 'a', 'b', 'c', 'b', 'a']
lps = LongestPalindromicSubSequence(data)
print("Bruce result:", lps.bruce(), ", time take:", timeit.timeit("LongestPalindromicSubSequence(['d', 'a', 'b', 'c', 'b', 'a']).bruce()", setup="from __main__ import LongestPalindromicSubSequence", number=10000))
print("Bruce result:", lps.dp(), ", time take:", timeit.timeit("LongestPalindromicSubSequence(['d', 'a', 'b', 'c', 'b', 'a']).dp()", setup="from __main__ import LongestPalindromicSubSequence", number=10000))
