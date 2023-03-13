n, k = map(int, input().split())
chess = []
for _ in range(n):
    chess.append(list(map(int, input().split())))

board = [[[] for _ in range(n)] for _ in range(n)]
mark = {}
for i in range(1, k+1):
    y, x, d = map(int, input().split())
    mark[i] = [y-1, x-1, d-1, 0]
    board[y-1][x-1].append(i)

dx = [1, -1, 0, 0]   # 동, 서, 북, 남 
dy = [0, 0, -1, 1]

answer = 1
while answer != 9:
    if answer > 1000:
        break

    for i in range(n):
        print(board[i])
    print('-------')

    end = False
    for i in range(1, k+1):
        y, x, d, h = mark[i]
        ny = y + dy[d]
        nx = x + dx[d]

        # 체스판 벗어나는 경우 and 파란색 
        if ny >=n or nx >= n or nx < 0 or ny < 0 or chess[ny][nx] == 2:
            if d == 0 or d == 2:
                d += 1
            else:
                d -= 1

            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < n and 0 <= nx < n:
                if chess[ny][nx] == 0:
                    nh = len(board[ny][nx])
                    for j in range(h, len(board[y][x])):
                        nd = mark[board[y][x][j]][2]
                        mark[board[y][x][j]] = [ny, nx, nd, nh]
                        board[ny][nx].append(board[y][x][j])
                        nh += 1
                        
                    board[y][x] = board[y][x][:h]
                    
                elif chess[ny][nx] == 1:
                    nh = len(board[ny][nx])
                    temp = board[y][x][h:]
                    temp.reverse()
                    for j in range(len(temp)):
                        nd = mark[temp[j]][2]
                        mark[temp[j]] = [ny, nx, nd, nh]
                        board[ny][nx].append(temp[j])
                        nh += 1
                    
                    board[y][x] = board[y][x][:h]
                    
                else:
                    mark[i] = [y, x, d, h]

            else:
                mark[i] = [y, x, d, h]

        # 흰색 
        elif chess[ny][nx] == 0:
            nh = len(board[ny][nx])
            for j in range(h, len(board[y][x])):
                nd = mark[board[y][x][j]][2]
                mark[board[y][x][j]] = [ny, nx, nd, nh]
                board[ny][nx].append(board[y][x][j])
                nh += 1
                    
            board[y][x] = board[y][x][:h]

        # 빨간색 
        else:
            nh = len(board[ny][nx])
            temp = board[y][x][h:]
            temp.reverse()
            for j in range(len(temp)):
                nd = mark[temp[j]][2]
                mark[temp[j]] = [ny, nx, nd, nh]
                board[ny][nx].append(temp[j])
                nh += 1
                    
            board[y][x] = board[y][x][:h]

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
        
            
        

