def staff_table(table_arr, staff_arr):
    def find_table(priority_arr):
        for i in priority_arr:
            for j in range(len(table_arr)):
                if table_arr[j] == i:
                    table_arr[j] += 1
                    return j + 1
    result = []
    for x in staff_arr:
        pa = [1, 0] if x == 'M' else [0, 1]
        result.append(find_table(pa))
    return result


T = int(input())
for i in range(T):
    N = int(input())
    ta = input()
    M = int(input())
    sa = input()
    re = staff_table([int(x) for x in ta], [x for x in sa])
    for x in re:
        print(x)