from collections import deque
from itertools import combinations

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

virus = []
wall = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            wall += 1
        if board[i][j] == 2:
            virus.append([i, j])


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(active):
    q = deque()
    visited = [[-1] * n for _ in range(n)]
    result = 0

    for y, x in active:
        q.append([y, x])
        visited[y][x] = 0

    while q:
        y, x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if board[ny][nx] == 0 and visited[ny][nx] == -1:
                    q.append([ny, nx])
                    visited[ny][nx] = visited[y][x] + 1
                    result = max(result, visited[ny][nx])
                elif board[ny][nx] == 2 and visited[ny][nx] == -1:
                    q.append([ny, nx])
                    visited[ny][nx] = visited[y][x] + 1

    count = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1:
                count += 1

    if count != wall:
        return n * n
    else:
        return result


answer = n * n
for active in combinations(virus, m):
    answer = min(answer, bfs(active))

if answer == n * n:
    print(-1)
else:
    print(answer)
