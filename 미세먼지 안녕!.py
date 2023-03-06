import copy

r, c, t = map(int, input().split())
board = []
for _ in range(r):
    board.append(list(map(int, input().split())))

s, e = [-1, -1], [-1, -1]
for i in range(r):
    for j in range(c):
        if board[i][j] == -1:
            if s[0] == -1 and s[1] == -1:
                s = [i, j]
            else:
                e = [i, j]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# 미세먼지 확산
def spread():
    arr = copy.deepcopy(board)
    
    for y in range(r):
        for x in range(c):
            if board[y][x] != 0 and board[y][x] != -1:
                cnt, temp = 0, board[y][x] // 5
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < c and 0 <= ny < r and board[ny][nx] != -1:
                        arr[ny][nx] += temp
                        cnt += 1

                arr[y][x] -= temp * cnt

    return arr


# 공기청정기 작동 
def clean():
    # 시계방향 
    y, x, d = s[0], s[1], 0
    save = 0
    
    while True:
        if y + dy[d] < 0 or x + dx[d] < 0 or y + dy[d] >= r or x + dx[d] >= c:
            d += 1

        ny = y + dy[d]
        nx = x + dx[d]

        if ny == s[0] and nx == s[1]:
            break
        
        save, board[ny][nx] = board[ny][nx], save
        y, x = ny, nx

    # 반시계 방향 
    y, x, d = e[0], e[1], 0
    save = 0
    
    while True:
        if y + dy[d] < 0 or x + dx[d] < 0 or y + dy[d] >= r or x + dx[d] >= c:
            d = (d - 1) % 4

        ny = y + dy[d]
        nx = x + dx[d]

        if ny == e[0] and nx == e[1]:
            break
        
        save, board[ny][nx] = board[ny][nx], save
        y, x = ny, nx

        
for _ in range(t):
    board = spread()
    clean()
    
answer = 0
for i in range(r):
    answer += sum(board[i])

print(answer+2)
