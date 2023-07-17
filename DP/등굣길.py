# link: https://school.programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    sol = [[[0, 0] for _ in range(n)] for _ in range(m)]
    for i in range(1, n):
        sol[0][i][0] = i
        sol[0][i][1] = 1
    for j in range(1, m):
        sol[j][0][0] = j
        sol[j][0][1] = 1
    for i, j in puddles:
        i, j = i - 1, j - 1
        sol[i][j][0] = 1e+12
        sol[i][j][1] = -1
        if i == 0:
            for k in range(j + 1, n):
                sol[0][k] = [1e+12, -1]
        if j == 0:
            for k in range(i + 1, m):
                sol[k][0] = [1e+12, -1]
                
    for i in range(1, m):
        for j in range(1, n):
            if sol[i][j][1] == -1:
                continue
            top = sol[i - 1][j]
            left = sol[i][j - 1]
            if top[0] < left[0]:
                sol[i][j][0], sol[i][j][1] = top[0] + 1, top[1]
            elif top[0] > left[0]:
                sol[i][j][0], sol[i][j][1] = left[0] + 1, left[1]
            else:
                sol[i][j][0], sol[i][j][1] = top[0] + 1, top[1] + left[1]         
    answer = sol[m - 1][n - 1][1]
    if answer < 0:
        return 0
    return answer % 1000000007
