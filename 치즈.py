import copy

n, m = map(int, input().split())
cheese = []
for _ in range(n):
    cheese.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visited = [[0] * m for _ in range(n)]

def bfs(y, x, t):
    q = []
    q.append([y, x])
    visited[y][x] = 1

    while q:
        y, x = q.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if cheese[ny][nx] == 0 and t == 1:
                    melt[ny][nx] = 2

                if cheese[ny][nx] == 0 and t == 2:
                    melt[ny][nx] = 0


melt = copy.deepcopy(cheese)
for i in range(n):
    for j in range(m):
        if cheese[i][j] == 0:
            bfs(i, j, 1)

for i in range(n):
    for j in range(m):
        if cheese[i][j] == 0:
            bfs(i, j, 2)

for i in range(n):
    print(melt[i])
                
