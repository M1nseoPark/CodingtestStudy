n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
size, c, d = 1, 0, 0

move = {(-2,0):0.02, (-1,-1):0.10, (-1,0):0.07, (-1,1):0.01, (0,-2):0.05,
        (1,-1):0.10, (1,0):0.07, (1,1):0.01, (2,0):0.02, (0,-1):0.55}

y, x = n//2+1, n//2+1
answer = 0

while True:
    if y == 0 and x == 0:
        break

    for i in range(size):
        y += dy[d]
        x += dx[d]
        
        sand = board[y][x]
        board[y][x] = 0
        
        for k, v in move.items():
            ny = y + k[0]
            nx = x + k[1]

            if 0 > ny or 0 > nx or ny >= n or nx >= n:
                answer += int(sand * v)
            else:
                board[ny][nx] += int(sand * v)

    c += 1
    d = (d + 1) % 4
    if c == 2:
        c = 0
        size += 1

    print(y, x)
    for i in range(n):
        print(board[i])
        
print(answer)
