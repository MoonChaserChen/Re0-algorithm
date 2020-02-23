def majority_element(nums: [int]) -> int:
    m1, s1 = None, 0
    m2, s2 = None, 0
    for x in nums:
        if s1 == 0 and m2 != x: m1 = x
        elif s2 == 0 and m1 != x: m2 = x
        if x == m1: s1 += 1
        elif x == m2: s2 += 1
        else: s1, s2 = s1 - 1, s2 - 1
    c1, c2 = 0, 0
    for x in nums:
        if x == m1: c1 += 1
        elif x == m2: c2 += 1
    re = []
    if c1 > len(nums) // 3: re.append(m1)
    if c2 > len(nums) // 3: re.append(m2)
    return re



print(majority_element([1, 2, 2, 3, 2, 1, 1, 3]))
