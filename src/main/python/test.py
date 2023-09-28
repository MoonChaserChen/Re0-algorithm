def next_greater_element(nums1, nums2):
    # 依次求nums2中每个元素的右侧第一个比它大的数，组成个map。再遍历nums1从这个map中取值即可
    # 倒着遍历nums2：
    # 如果下个数比当前数num更大，则当前数肯定不会是接下来的任一数的结果，可以忽略；这个操作可以重复，比如 [1, 4, 3, 2]，遍历到4时，3和2其实都可以抛弃（因为求第一个更大的数，如果能够选3和2，那么也可以选4）
    # 用一个栈来保存上面的数，对当前数num来说，第一个不能抛弃的数即为num的结果。
    m = {}
    stack = []
    for num in nums2:
        while stack and num > stack[-1]:
            stack.pop()
        m[num] = stack[-1] if stack else -1
        stack.append(num)
    return [m[x] for x in nums1]