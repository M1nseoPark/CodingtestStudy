n, k = map(int, input().split())
chess = []
for _ in range(n):
    chess.append(list(map(int, input().split())))

board = [[[] for _ in range(n)] for _ in range(n)]
mark = {}
for i in range(1, k+1):
    y, x, d = map(int, input().split())
    mark[i] = [y-1, x-1, d-1]
    board[y-1][x-1].append(i)

dx = [1, -1, 0, 0]   # 동, 서, 북, 남 
dy = [0, 0, -1, 1]

answer = 1
while True:
    if answer > 1000:
        break

    end = False
    for i in range(1, k+1):
        y, x, d = mark[i]
        ny = y + dy[d]
        nx = x + dx[d]

        # 체스판 벗어나는 경우 or 파란색 
        if ny >=n or nx >= n or nx < 0 or ny < 0 or chess[ny][nx] == 2:
            if d == 0 or d == 2:
                d += 1
            else:
                d -= 1

            ny = y + dy[d]
            nx = x + dx[d]
            if ny >= n or nx >= n or nx < 0 or ny < 0 or chess[ny][nx] == 2:
                nx = x
                ny = y

        mark[i] = [ny, nx, d]
        if ny == y and nx == x:
            continue

        idx = board[y][x].index(i)
        # 해당 말 위에 있던 말 이동
        for j in board[y][x][idx+1:]:   
            mark[j][0] = ny
            mark[j][1] = nx

        # 옮긴 뒤의 색이 하얀색
        if chess[ny][nx] == 0:
            board[ny][nx] += board[y][x][idx:]

        # 옮긴 뒤의 색이 빨간색
        elif chess[ny][nx] == 1:
            board[ny][nx] += board[y][x][idx:][::-1]

        board[y][x] = board[y][x][:idx]

        if 0 <= ny < n and 0 <= nx < n and len(board[ny][nx]) >= 4:
            end = True
            break

    if end:
        break

    answer += 1


if answer > 1000:
    print(-1)
else:
    print(answer)
        
            
        

