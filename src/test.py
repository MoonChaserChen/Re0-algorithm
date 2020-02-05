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
    return lo


arr0 = [1, 2, 3, 4, 6, 7, 8, 9, 10]
for x in arr0:
    print(bi_search(arr0, x))
print(bi_search(arr0, 0))
print(bi_search(arr0, 11))
print(bi_search(arr0, 5))