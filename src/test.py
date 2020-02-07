def my_sqrt(x):
    """
    :type x: int
    :rtype: int
    """
    if x <= 1: return x
    lo, hi = 0, x
    while lo <= hi:
        mid = (lo + hi) // 2
        v = x // mid
        if v == mid:
            return mid
        elif  v > mid:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo - 1