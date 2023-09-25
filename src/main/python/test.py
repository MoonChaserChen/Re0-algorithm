def rotate(matrix):
    n = len(matrix)
    for i in range((n + 1) // 2):
        for j in range(n // 2):
            matrix[i][j], matrix[n -1 - j][i], matrix[n - 1 - i][n - 1 - j], matrix[j][n - 1 - i] = \
                matrix[n -1 - j][i], matrix[n - 1 - i][n - 1 - j], matrix[j][n - 1 - i], matrix[i][j]
    return matrix


assert rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
assert rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]) == [[15, 13, 2, 5], [14, 3, 4, 1],
                                                                                   [12, 6, 8, 9], [16, 7, 10, 11]]
