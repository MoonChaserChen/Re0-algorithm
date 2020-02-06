def three_sum(nums):
    re_dic = {}
    for i in range(len(nums) - 1):
        curr = nums[i]
        if not re_dic.get(curr):
            re_dic[curr] = two_sum(nums[i + 1:], -curr, re_dic)
    re = []
    for x in re_dic:
        arr = re_dic[x]
        if arr:
            for y in arr:
                re.append([x, y[0], y[1]])
    return re


def two_sum(nums, target, except_dic):
    x_dic = {} # “差值字典”，保存未匹配上时的： x: target-x
    re_dic = {} # 利用字典过滤相同的结果
    for x in nums:
        rem = target - x
        # except_dic存放three_sum时已经遍历过的值，这里不能再使用了，否则会导致重复
        # 如：[-1, 0, 1, 2, -1, -4] 在three_sum遍历-1时匹配上了[-1, 0, 1]，-1会被存放在except_dic中，这样就会排除后序出现的 [0, 1, -1]了
        if x in except_dic or rem in except_dic:
            continue
        if rem in x_dic:
            # 匹配上时，存入结果字典；一旦匹配上，x将不能再使用了，因此不存入x_dic
            re_dic[rem] = x
        else:
            # 未匹配上时，存入“差值字典”
            x_dic[x] = rem
    re = []
    for k in re_dic:
        re.append([k, re_dic[k]])
    return re

print(three_sum([-1, 0, 1, 2, -1, -4]))