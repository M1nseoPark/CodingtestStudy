import sys
sys.setrecursionlimit(10000)

m, n, k = map(int, input().split())

square = [[0] * n for _ in range(m)]
for _ in range(k):
    a, b, c, d = map(int, input().split())

    # 이거 구하는게 어려웠음..
    lx = a
    rx = c
    ly = m - d
    ry = m - b

    for i in range(ly, ry):
        for j in range(lx, rx):
            square[i][j] = 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(y, x):
    global temp
    square[y][x] = 1
    temp += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and square[ny][nx] == 0:
            dfs(ny, nx)
            

answer = []
temp = 0
for i in range(m):
    for j in range(n):
        if square[i][j] == 0:
            dfs(i, j)
            answer.append(temp)
            temp = 0

print(len(answer))
answer.sort()

for i in answer:
    print(i, end=' ')

            

