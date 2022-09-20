import sys
sys.setrecursionlimit(10000) 

test = int(input())

def dfs(x, y):
    if x < 0 or x >= m or y < 0 or y >= n:
        return False

    if farm[x][y] == 1:
        farm[x][y] = 0

        for i in range(4):
            for j in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                dfs(nx, ny)

        return True

    else:
        return False

    
for t in range(test):
    m, n, k = map(int, input().split())

    farm = [[0] * n for _ in range(m)]   # x, y
    for _ in range(k):
        a, b = map(int, input().split())
        farm[a][b] = 1

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    answer = 0
    for i in range(m):
        for j in range(n):
            if dfs(i, j):
                answer += 1

    print(answer)
                

