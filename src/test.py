def set_zeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    m, n = len(matrix), len(matrix[0])
    # 首列是否原本存在0
    flag_col0 = False

    # 用matrix首行/列保存当前列/行是否存在0
    for i in range(m):
        if matrix[i][0] == 0:
            flag_col0 = True
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0

    for i in range(m - 1, -1, -1):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
        if flag_col0:
            matrix[i][0] = 0


mt = [[0, 1, 2, 0],
      [3, 4, 5, 2],
      [1, 3, 1, 5]]
print(mt)
set_zeroes(mt)
print(mt)
