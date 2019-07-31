def bubble_sort(arr):
    le = len(arr)
    for i in range(le - 1):
        is_sorted = 1
        for j in range(le - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_sorted = 0
        if is_sorted:
            return arr
    return arr


print(bubble_sort([1, 5, 3, 6, 4, 8, 2]))
