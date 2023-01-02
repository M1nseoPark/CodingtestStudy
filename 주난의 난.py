from collections import deque

n, m = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
room = []
for _ in range(n):
    room.append(list(input()))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs():
    q = deque()
    q.append([x1-1, y1-1])
    visited = [[-1] * m for _ in range(n)]
    visited[x1-1][y1-1] = 0

    while q:
        y, x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == -1:
                if room[ny][nx] == '1' or room[ny][nx] == '#':
                    q.append([ny, nx])
                    visited[ny][nx] = visited[y][x] + 1
                else:
                    q.appendleft([ny, nx])
                    visited[ny][nx] = visited[y][x]

    return visited[x2-1][y2-1]

print(bfs())
