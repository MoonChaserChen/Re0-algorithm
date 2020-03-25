def surface_area(grid: [[int]]) -> int:
    n = len(grid)
    s = 0
    for i in range(n):
        for j in range(n):
            v = grid[i][j]
            for k in range(v):
                s += 6
                if v > 1:
                    s -= (1 if k == 0 or k == v - 1 else 2)
                if i > 0 and grid[i - 1][j] > k:
                    s -= 1
                if i < n - 1 and grid[i + 1][j] > k:
                    s -= 1
                if j > 0 and grid[i][j - 1] > k:
                    s -= 1
                if j < n - 1 and grid[i][j + 1] > k:
                    s -= 1
    return s


grids = [[1, 2], [3, 4]]
print(surface_area(grids))
