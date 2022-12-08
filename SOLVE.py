from collections import deque
from itertools import combinations
import copy

n, m = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

sub = []

for i in range(n):
    for j in range(m):
        if maps[i][j] == 0:
            sub.append([i, j])


def bfs(temp):
    safe = 0
    q = deque()

    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                q.append([i, j])
    
    while q:
        y, x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and temp[ny][nx] != 0:
                temp[ny][nx] = 2
                q.append([ny, nx])


    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                safe += 1

    return safe
            

answer = 0
for s in list(combinations(sub, 3)):
    temp = copy.deepcopy(maps)

    for i in range(3):
        sy, sx = s[i][0], s[i][1]
        temp[sy][sx] = 1

    answer = max(answer, bfs(temp))

print(answer)




