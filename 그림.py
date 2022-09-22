# DFS로는 안풀리는 문제인듯

import sys
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())
draw = []

for i in range(n):
    draw.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(y, x):
    draw[y][x] = 0
    global area
    area += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n and draw[ny][nx] == 1:
            dfs(ny, nx)


area = 0
answer = []
for i in range(n):
    for j in range(m):
        if draw[i][j] == 1:
            dfs(i, j)
            answer.append(area)
            area = 0

if len(answer) == 0:
    print(0)
    print(0)
else:
    print(len(answer))
    print(max(answer))
            
