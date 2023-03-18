from collections import deque

n, m, gas = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))
by, bx = map(int, input().split())
by -= 1; bx -= 1
client = {}
for i in range(1, m+1):
    a, b, c, d = map(int, input().split())
    client[(a-1, b-1)] = [c-1, d-1]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def decide():
    q = deque()
    q.append([by, bx])
    visited = [[-1] * n for _ in range(n)]
    visited[by][bx] = 0
    cnt = 0

    while q:
        y, x = q.popleft()

        if cnt == len(client):
            break

        if (y, x) in client:
            val = client[(y, x)]
            sub.append([visited[y][x], y, x, val[0], val[1]])
            cnt += 1

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and maps[ny][nx] == 0 and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                q.append([ny, nx])


def bfs(cy, cx):
    q = deque()
    q.append([by, bx])
    visited = [[-1] * n for _ in range(n)]
    visited[by][bx] = 0

    while q:
        y, x = q.popleft()

        if y == cy and x == cx:
            return visited[y][x]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and maps[ny][nx] == 0 and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                q.append([ny, nx])

    return -1


for _ in range(m):
    sub = []   # [visited[y][x], y, x, val[0], val[1]]
    decide()
    sub.sort(key=lambda x:(x[0], x[1], x[2]))
    
    if len(sub) == 0 or sub[0][0] > gas:
        gas = -1
        break

    gas -= sub[0][0]
    del client[(sub[0][1], sub[0][2])]
    by, bx = sub[0][1], sub[0][2]

    d = bfs(sub[0][3], sub[0][4])
    if d == -1 or d > gas:
        gas = -1
        break

    gas -= d
    gas += d * 2
    by, bx = sub[0][3], sub[0][4]

print(gas)

    
        
