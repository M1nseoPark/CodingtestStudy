# 3차원 배열 문제를 2차원 배열로 풀면 안된다!
import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())
box = [[] for _ in range(h)]
for i in range(h):
    for _ in range(n):
        box[i].append(list(map(int, sys.stdin.readline().split())))

dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
q = deque()

for k in range(h):
    for i in range(n):
        for j in range(m):
            if box[k][i][j] == 1:
                q.append([k, i, j])

def bfs():
    while q:
        z, y, x = q.popleft()
        
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
                if box[nz][ny][nx] == 0:
                    box[nz][ny][nx] = box[z][y][x] + 1
                    q.append([nz, ny, nx])

bfs()
answer = 0
ripe = True

for k in range(h):
    for i in range(n):
        for j in range(m):
            if box[k][i][j] != 0:
                answer = max(answer, box[k][i][j])
            else:
                ripe = False

if not ripe:
    print(-1)
else:
    print(answer - 1)
    

