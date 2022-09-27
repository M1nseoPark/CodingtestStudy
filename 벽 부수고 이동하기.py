from collections import deque
import sys

# 좌표 -1
n, m = map(int, sys.stdin.readline().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0] * m for _ in range(n)]
           

def bfs():
    visited = [[0] * m for _ in range(n)]
    q = deque()
    q.append([0, 0])

    while q:
        y, x = q.popleft()

        if y == (n - 1) and x == (m - 1):
            answer.append(visited[y][x])
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 0 and visited[ny][nx] == 0:
                q.append([ny, nx])
                visited[ny][nx] = visited[y][x] + 1
    
    
def make():
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1:
                maps[i][j] = 0
                bfs()
                maps[i][j] = 1

answer = []
make()

if len(answer) == 0:
    print(-1)
else:
    print(min(answer) + 1)


