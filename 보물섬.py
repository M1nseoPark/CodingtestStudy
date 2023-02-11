from collections import deque
import sys

r, c = map(int, sys.stdin.readline().split())
maps = []
for _ in range(r):
    maps.append(list(sys.stdin.readline().rstrip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(y, x):
    q = deque()
    q.append([y, x])
    visited = [[-1] * c for _ in range(r)]
    visited[y][x] = 0
    cnt = 0

    while q:
        y, x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < c and 0 <= ny < r and visited[ny][nx] == -1 and maps[ny][nx] == 'L':
                visited[ny][nx] = visited[y][x] + 1
                if visited[ny][nx] > cnt:
                    cnt = visited[ny][nx]
                q.append([ny, nx])

    return cnt


answer = 0
for i in range(r):
    for j in range(c):
        if maps[i][j] == 'L':
            answer = max(answer, bfs(i, j))

print(answer)
    
                
