def fast_sort(arr):
    # 将arr数组中left_index到right_index中right_index放置到正确的位置，并且放置后right_index左侧的数均要小，右侧数均要大
    def partition(left_index, right_index):
        swapping_index = left_index
        pivot_index = right_index
        for i in range(left_index, right_index):
            if arr[i] < arr[pivot_index]:
                arr[swapping_index], arr[i] = arr[i], arr[swapping_index]
                swapping_index += 1
        arr[swapping_index], arr[pivot_index] = arr[pivot_index], arr[swapping_index]
        return swapping_index

    # 递归做partition操作，最终使得index位于[left_index, right_index]间所有值都在正确的位置
    def sort(left_index, right_index):
        if left_index < right_index:
            # 将right_index放置到正确的位置后，迭代处理两边的数据
            sep = partition(left_index, right_index)
            sort(left_index, sep - 1)
            sort(sep + 1, right_index)
    sort(0, len(arr) - 1)
    return arr


print(fast_sort([1, 5, 3, 6, 4, 8, 2]))
