from itertools import combinations
from collections import deque

n, m = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

virus = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 2:
            virus.append([i, j])

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(v):
    visited = [[-1] * n for _ in range(n)]
    q = deque()
    result = 0
    
    for i in range(m):
        y, x = v[i][0], v[i][1]
        visited[y][x] = 0
        q.append([y, x])

    while q:
        y, x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and maps[ny][nx] != 1 and visited[ny][nx] == -1:
                q.append([ny, nx])
                visited[ny][nx] = visited[y][x] + 1


    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1:
                if maps[i][j] != 1:
                    result = -1
                    break

            else:
                result = max(result, visited[i][j])

        if result == -1:
            break


    return result

        
answer = 10000
for v in list(combinations(virus, m)):
    temp = bfs(v)
    if temp != -1:
        answer = min(answer, temp)


if answer == 10000:
    print(-1)
else:
    print(answer)
