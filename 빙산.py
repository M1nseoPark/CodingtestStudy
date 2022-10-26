from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
sea = []
for _ in range(n):
    sea.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
time = 0

def bfs(y, x):
    q = deque()
    q.append([y, x])
    visited[y][x] = 1

    while q:
        y, x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if visited[ny][nx] == 0:
                    if sea[ny][nx] != 0:
                        visited[ny][nx] = 1
                        q.append([ny, nx])
                    else:
                        visited[ny][nx] = 1
                        pick[y][x] += 1
    

while True:
    pick = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    result = 0

    for i in range(n):
        for j in range(m):
            if sea[i][j] != 0 and visited[i][j] == 0:
                bfs(i, j)
                result += 1

    if result == 0:
        print(0)
        break

    if result >= 2:
        print(time)
        break


    for i in range(n):
        for j in range(m):
            if pick[i][j] != 0:
                if sea[i][j] < pick[i][j]:
                    sea[i][j] = 0
                else:
                    sea[i][j] -= pick[i][j]

    time += 1
    
