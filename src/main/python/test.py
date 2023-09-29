def next_greater_element(nums1, nums2):
    stack = []
    m = {}
    for i in range(len(nums2)):
        while stack and nums2[stack[-1]] < nums2[i]:
            m[nums2[stack.pop()]] = nums2[i]
        stack.append(i)
    return [m.get(x, -1) for x in nums1]


assert next_greater_element([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]
assert next_greater_element([2, 4], [1, 2, 3, 4]) == [3, -1]
