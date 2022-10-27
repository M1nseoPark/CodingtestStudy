# 벽 부수기 문제랑 비슷! -> 3차원 visited 리스트를 사용해야 함

from collections import deque

k = int(input())
w, h = map(int, input().split())

board = []
for _ in range(h):
    board.append(list(map(int, input().split())))

dy = [-2, -2, -1, -1, 1, 1, 2, 2, -1, 1, 0, 0]
dx = [-1, 1, -2, 2, -2, 2, -1, 1, 0, 0, -1, 1]

def bfs():
    while q:
        y, x, z = q.popleft()

        if y == (h - 1) and x == (w - 1):
            return visited[y][x][z]

        if z < k:
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < w and 0 <= ny < h:
                    if board[ny][nx] == 0 and visited[ny][nx][z+1] == 0:
                        q.append([ny, nx, z+1])
                        visited[ny][nx][z+1] = visited[y][x][z] + 1

        for i in range(8, 12):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < w and 0 <= ny < h:
                if board[ny][nx] == 0 and visited[ny][nx][z] == 0:
                    q.append([ny, nx, z])
                    visited[ny][nx][z] = visited[y][x][z] + 1

    return -1
                
                                    
q = deque()
q.append([0, 0, 0])
visited = [[[0] * 31 for _ in range(w)] for _ in range(h)]
print(bfs())
    
