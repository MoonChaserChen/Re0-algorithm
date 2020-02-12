def generate(num_rows: int) -> list:
    re = []
    for i in range(num_rows):
        level_re = []
        for j in range(i + 1):
            if j == 0 or j == i:
                level_re.append(1)
            else:
                level_re.append(re[i - 1][j - 1] + re[i - 1][j])
        re.append(level_re)
    return re