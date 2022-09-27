test = int(input())

dx = [-1, 1, -2, 2, -2, 2, -1, 1]
dy = [-2, -2, -1, -1, 1, 1, 2, 2]


def bfs(y, x):
    global i, py, px
    q = []
    q.append([y, x])

    while q:
        y, x = q.pop(0)

        if y == py and x == px:
            break
        
        for j in range(8):
            nx = x + dx[j]
            ny = y + dy[j]
            if 0 <= nx < i and 0 <= ny < i and move[ny][nx] == 0:
                q.append([ny, nx])
                move[ny][nx] = move[y][x] + 1

                
for _ in range(test):
    i = int(input())
    cx, cy = map(int, input().split())
    px, py = map(int, input().split())

    move = [[0] * i for _ in range(i)]
    
    bfs(cy, cx)
    print(move[py][px])


    
    
    
