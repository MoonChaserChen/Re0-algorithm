def next_greater_element(num):
    arr = list(str(num))
    n = len(arr)
    s_i = n - 2
    while s_i >= 0 and arr[s_i] >= arr[s_i + 1]:
        s_i -= 1
    if s_i >= 0:
        b_i = n - 1
        while arr[b_i] <= arr[s_i]:
            b_i -= 1
        arr[s_i], arr[b_i] = arr[b_i], arr[s_i]
    else:
        return -1
    lo, hi = s_i + 1, n - 1
    while lo < hi:
        arr[lo], arr[hi] = arr[hi], arr[lo]
        lo += 1
        hi -= 1
    result = int("".join(arr))
    return -1 if result > 2 ** 31 - 1 else result

assert next_greater_element(12) == 21
assert next_greater_element(21) == -1
