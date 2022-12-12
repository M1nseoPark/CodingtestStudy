from itertools import combinations
import copy
from collections import deque

n, m = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

virus = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(n):
        if maps[i][j] == 2:
            virus.append([i, j])


def bfs(temp, v):
    q = deque()
    distance = [[-1] * n for _ in range(n)]
    time = 0

    for i in range(m):
        y, x = v[i][0], v[i][1]
        temp[y][x] = 3
        q.append([y, x])
        distance[y][x] = 0
        

    while q:
        y, x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if temp[ny][nx] == 0:
                    temp[ny][nx] = 3
                    distance[ny][nx] = distance[y][x] + 1
                    time = max(time, distance[ny][nx])
                    q.append([ny, nx])
               
                elif temp[ny][nx] == 2:
                    temp[ny][nx] = 3
                    distance[ny][nx] = distance[y][x] + 1
                    q.append([ny, nx])
                    

    finish = True
    for i in range(n):
        for j in range(n):
            if temp[i][j] == 0:
                finish = False
                break

    if finish:
        return time
    else:
        return n * n
    

answer = n * n

for v in list(combinations(virus, m)):
    temp = copy.deepcopy(maps)
    answer = min(bfs(temp, v), answer)

if answer == n * n:
    print(-1)
else:
    print(answer)
        
        
    
