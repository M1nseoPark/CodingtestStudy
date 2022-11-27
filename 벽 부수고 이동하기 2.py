from collections import deque
import sys


n, m, k = map(int, sys.stdin.readline().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().rstrip())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
            

def bfs():
    q = deque()
    q.append([0, 0, 0])
    visited = [[[0] * (k+1) for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1

    while q:
        y, x, z = q.popleft()

        if y == n - 1 and x == m - 1:
            return visited[y][x][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if visited[ny][nx][z] == 0 and maps[ny][nx] == 0:
                    q.append([ny, nx, z])
                    visited[ny][nx][z] = visited[y][x][z] + 1

                if z < k and maps[ny][nx] == 1 and visited[ny][nx][z+1] == 0:
                    q.append([ny, nx, z+1])
                    visited[ny][nx][z+1] = visited[y][x][z] + 1

    return -1


print(bfs())

