def bi_search(arr, e):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == e:
            return mid
        elif arr[mid] < e:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

print(bi_search([1, 3, 4, 5, 6, 7, 8, 10, 11, 12, 14], 10))


