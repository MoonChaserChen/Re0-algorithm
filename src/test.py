def majority_element(nums: [int]) -> int:
    s, majority = 0, None
    for x in nums:
        if s == 0: majority = x
        if x != majority: s-= 1
        else: s += 1
    return majority

print(majority_element([1, 2, 3, 2, 2, 1]))