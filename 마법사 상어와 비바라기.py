n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

cdy = [0, -1, -1, -1, 0, 1, 1, 1]   # 구름 이동
cdx = [-1, -1, 0, 1, 1, 1, 0, -1]
wdy = [-1, -1, 1, 1]   # 물복사버그 
wdx = [-1, 1, -1, 1]

cloud = {(n-1, 0): 1, (n-1, 1): 1, (n-2, 0): 1, (n-2, 1): 1}

for _ in range(m):
    d, s = map(int, input().split())
    d -= 1

    move = {}
    for k, v in cloud.items():
        y, x = k[0], k[1]
        ny = (y + cdy[d]*s) % n
        nx = (x + cdx[d]*s) % n
        move[(ny, nx)] = 1
        board[ny][nx] += 1   # 구름이 있는 바구니 물의 양 1 증가

    cloud = {}   # 구름이 모두 사라짐
    
    # 물복사버그 마법 시전 
    for k, v in move.items():
        y, x = k[0], k[1]
        t = 0
        for i in range(4):
            ny = y + wdy[i]
            nx = x + wdx[i]
            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] >= 1:
                t += 1
        board[y][x] += t

    for i in range(n):
        for j in range(n):
            if board[i][j] >= 2 and (i, j) not in move:
                board[i][j] -= 2
                cloud[(i, j)] = 1

answer = 0
for i in range(n):
    for j in range(n):
        answer += board[i][j]

print(answer)

    
