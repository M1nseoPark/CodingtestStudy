from collections import deque

n, m = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
fy, fx = 0, 0

for i in range(n):
    for j in range(m):
        if maps[i][j] == 2:
            fy, fx = i, j

q = deque()
q.append([fy, fx])
visited = [[0] * m for _ in range(n)]

while q:
    y, x = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == 0 and maps[ny][nx] == 1:
            visited[ny][nx] = visited[y][x] + 1
            q.append([ny, nx])

for i in range(n):
    for j in range(m):
        if maps[i][j] == 1 and visited[i][j] == 0:
            print(-1, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()
            
        
