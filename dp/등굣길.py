def solution(m, n, puddles):
    matrix = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if [j, i] in puddles:
                continue
            if i == 1 and j == 1:
                matrix[i][j] = 1
            else:
                matrix[i][j] = (matrix[i - 1][j] + matrix[i][j - 1]) % 1_000_000_007

    return matrix[n][m]
