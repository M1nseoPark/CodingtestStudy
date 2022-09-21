import sys
sys.setrecursionlimit(1000000)

n = int(input())
rain = []

k = 0
for i in range(n):
    rain.append(list(map(int, input().split())))
    k = max(k, max(rain[i]))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(y, x, r):
    visited[y][x] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == 0 and r < rain[ny][nx]:
            dfs(ny, nx, r)


answer = 0
for r in range(k):
    visited = [[0] * n for _ in range(n)]
    temp = 0
    
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and r < rain[i][j]:
                temp += 1
                dfs(i, j, r)

    if temp >= answer:
        answer = temp

print(answer)
