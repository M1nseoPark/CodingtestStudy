from collections import deque

n, m = map(int, input().split())
soldier = []
for _ in range(m):
    soldier.append(list(input()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(y, x):
    q = deque()
    q.append([y, x])
    visited[y][x] = 1
    temp = 1

    while q:
        y, x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if soldier[y][x] == soldier[ny][nx] and visited[ny][nx] == 0:
                    q.append([ny, nx])
                    visited[ny][nx] = 1
                    temp += 1
                    
    return temp ** 2

white = 0
visited = [[0] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if soldier[i][j] == 'W' and visited[i][j] == 0:
            white += bfs(i, j)

blue = 0
visited = [[0] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if soldier[i][j] == 'B' and visited[i][j] == 0:
            blue += bfs(i, j)

print(white, blue)
