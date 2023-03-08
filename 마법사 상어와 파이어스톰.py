from collections import deque
import copy

n, q = map(int, input().split())   # 2^nx2^n, 파이어스톰 q번 시전
ice = []
m = 2**n
for _ in range(m):
    ice.append(list(map(int, input().split())))
L = list(map(int, input().split()))   # 부분 격자의 크기

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for t in range(q):
    l = 2**L[t]
    rice = [[0] * m for _ in range(m)]
    
    for y in range(0, m, l):
        for x in range(0, m, l):
            for i in range(l):
                for j in range(l):
                    rice[y+j][x+l-i-1] = ice[y+i][x+j]

    ice = copy.deepcopy(rice)

    for y in range(m):
        for x in range(m):
            if rice[y][x] > 0:
                cnt = 0
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if 0 <= ny < m and 0 <= nx < m and rice[ny][nx] > 0:
                        cnt += 1

                if cnt < 3:
                    ice[y][x] -= 1


ans1, ans2 = 0, 0
for i in range(m):
    for j in range(m):
        ans1 += ice[i][j]


def bfs(y, x):
    q = deque()
    q.append([y, x])
    visited[y][x] = 1
    cnt = 1

    while q:
        y, x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < m and ice[ny][nx] > 0 and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                q.append([ny, nx])
                cnt += 1

    return cnt
    

visited = [[0] * m for _ in range(m)]
for i in range(m):
    for j in range(m):
        if ice[i][j] > 0 and visited[i][j] == 0:
            ans2 = max(ans2, bfs(i, j))

print(ans1)
print(ans2)
