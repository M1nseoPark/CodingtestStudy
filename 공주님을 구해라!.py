from collections import deque

n, m, t = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs():
    q = deque()
    q.append([0, 0, 0])
    visited = [[[-1] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 0

    while q:
        y, x, g = q.popleft()

        if y == n - 1 and x == m - 1:
            print(visited[y][x][g])
            return

        if visited[y][x][g] > t:
            print('Fail')
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and visited[ny][nx][g] == -1:
                if g == 0:
                    if maps[ny][nx] == 0:
                        q.append([ny, nx, g])
                        visited[ny][nx][g] = visited[y][x][g] + 1
                    elif maps[ny][nx] == 2:
                        q.append([ny, nx, g+1])
                        visited[ny][nx][g+1] = visited[y][x][g] + 1

                else:
                    if maps[ny][nx] == 0 or maps[ny][nx] == 1:
                        q.append([ny, nx, g])
                        visited[ny][nx][g] = visited[y][x][g] + 1

    print('Fail')
    return

bfs()
        
    
