n = int(input())
picture = []
for _ in range(n):
    picture.append(list(input()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

visited = [[0] * n for _ in range(n)]

def bfs(y, x, c):
    q = []
    q.append([y, x])
    visited[y][x] = 1

    while q:
        y, x = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == 0 and picture[ny][nx] == c:
                visited[ny][nx] = 1
                q.append([ny, nx])


normal = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j, picture[i][j])
            normal += 1


for i in range(n):
    for j in range(n):
        if picture[i][j] == 'G':
            picture[i][j] = 'R'

visited = [[0] * n for _ in range(n)]
blind = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j, picture[i][j])
            blind += 1

print(normal, blind)
        
