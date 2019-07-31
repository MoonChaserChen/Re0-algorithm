def select_sort(arr):
    le = len(arr)
    for i in range(le - 1):
        min_index = i
        for j in range(i, le):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


print(select_sort([1, 5, 3, 6, 4, 8, 2]))
