from collections import deque

n = int(input())
maps = []
for _ in range(n):
    maps.append(list(map(int, input())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(y, x):
    q = deque()
    q.append([y, x])

    maps[y][x] = 2
    cnt = 1

    while q:
        y, x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and maps[ny][nx] == 1:
                maps[ny][nx] = 2
                q.append([ny, nx])
                cnt += 1
    
    return cnt


answer = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            answer.append(bfs(i, j))

print(len(answer))
answer.sort()
for i in answer:
    print(i)
