def three_sum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

def two_sum(nums, target):
    x_dic = {}
    re_dic = {}
    re = []
    for x in nums:
        rem = target - x
        if rem in x_dic:
            re_dic[rem] = x
        else:
            x_dic[x] = rem
    for k in re_dic:
        re.append([k, re_dic[k]])
    return re

print(two_sum([1, 2, 3, 4, 4, 4, 4, 5, 6, 7, 7, 1], 8)) # [[4, 4], [3, 5], [2, 6], [1, 7]]