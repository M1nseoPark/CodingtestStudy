from collections import deque

h, w = map(int, input().split())
sky = []
for _ in range(h):
    sky.append(list(input()))


def bfs(y, x):
    q = deque()
    q.append([y, x])
    visited[y][x] = 0

    while q:
        y, x = q.popleft()

        nx = x + 1
        ny = y
        if 0 <= nx < w and visited[ny][nx] == -1 and sky[ny][nx] == '.':
            visited[ny][nx] = visited[y][x] + 1
            q.append([ny, nx])


visited = [[-1] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if sky[i][j] == 'c' and visited[i][j] == -1:
            bfs(i, j)

for i in range(h):
    print(' '.join(map(str, visited[i])))
        
    
