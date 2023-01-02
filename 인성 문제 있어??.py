from collections import deque
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    h, w, o, f, xs, ys, xe, ye = map(int, sys.stdin.readline().split())
    maze = [[0] * (w + 1) for _ in range(h+1)]
    for i in range(o):
        x, y, l = map(int, sys.stdin.readline().split())
        maze[x][y] = l

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]


    def bfs():
        q = deque()
        q.append([xs, ys, f])
        visited = [[[-1] * (f + 1) for _ in range(w+1)] for _ in range(h+1)]
        visited[xs][ys][f] = 0

        while q:
            cx, cy, d = q.popleft()

            if cx == xe and cy == ye:
                print('잘했어!!')
                return

            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if 0 < nx <= h and 0 < ny <= w and visited[nx][ny][d] == -1 and d > 0:
                    if maze[cx][cy] >= maze[nx][ny]:
                        visited[nx][ny][d-1] = visited[cx][cy][d] + 1
                        q.append([nx, ny, d-1])

                    else:
                        if maze[nx][ny] - maze[cx][cy] <= d:
                            visited[nx][ny][d-1] = visited[cx][cy][d] + 1
                            q.append([nx, ny, d-1])

        print('인성 문제있어??')
        return

    bfs()

    
