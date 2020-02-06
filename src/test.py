def two_sum(nums, target):
    dic = {}
    re = []
    for x in nums:
        rem = target - x
        if rem in dic:
            re.append([x, rem])
        else:
            dic[x] = rem
    return re

def two_sum1(nums, target):
    dic = {}
    re = []
    for x in nums:
        rem = target - x
        if rem in dic:
            for y in dic[rem]:
                re.append([x, rem])
        arr = dic.get(x)
        if arr:
            arr.append(rem)
        else:
            dic[x] = [rem]
    return re

nums0 = [-9, -5, -4, 4, 5, 9, 0, 0, 0, 0]
print(two_sum(nums0, 0))
print(two_sum1(nums0, 0)) # [[4, -4], [5, -5], [9, -9], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
