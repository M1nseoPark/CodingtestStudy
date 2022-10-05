from collections import deque

n, m, k = map(int, input().split())
trash = [[0] * (m + 1) for _ in range(n+1)]

for _ in range(k):
    a, b = map(int, input().split())
    trash[a][b] = 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visited = [[0] * (m + 1) for _ in range(n+1)]

def bfs(y, x):
    global answer
    q = deque()
    q.append([y, x])
    visited[y][x] = 1
    result = 1

    while q:
        y, x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 1 <= nx < m+1 and 1 <= ny < n+1:
                if trash[ny][nx] == 1 and visited[ny][nx] == 0:
                    q.append([ny, nx])
                    visited[ny][nx] = 1
                    result += 1

    answer = max(answer, result)


answer = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if trash[i][j] == 1 and visited[i][j] == 0:
            bfs(i, j)

print(answer)

    


