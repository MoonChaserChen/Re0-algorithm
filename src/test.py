def find_duplicate(nums: list) -> int:
    slow, fast = 0, 0
    slow, fast = nums[slow], nums[nums[fast]]
    while slow != fast:
        slow, fast = nums[slow], nums[nums[fast]]
    n1, n2 = 0, slow
    while n1 != n2:
        n1, n2 = nums[n1], nums[n2]
    return n1