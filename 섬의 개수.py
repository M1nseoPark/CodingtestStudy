import sys
sys.setrecursionlimit(10000)

dx = [0, 0, -1, 1, -1, -1, 1, 1]
dy = [-1, 1, 0, 0, -1, 1, -1, 1]

def dfs(y, x):
    maps[y][x] = 0

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < w and 0 <= ny < h and maps[ny][nx] == 1:
            dfs(ny, nx)
            

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    maps = []
    for _ in range(h):
        maps.append(list(map(int, input().split())))

    answer = 0
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1:
                answer += 1
                dfs(i, j)

    print(answer)
                
