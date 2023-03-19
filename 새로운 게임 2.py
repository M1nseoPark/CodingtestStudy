n, k = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
mark = [[[] for _ in range(n)] for _ in range(n)]
dic = {}
for i in range(1, k+1):
    a, b, c = map(int, input().split())
    dic[i] = [a-1, b-1, c-1]
    mark[a-1][b-1].append(i)

dx = [1, -1, 0, 0]   # 동서북남 
dy = [0, 0, -1, 1]
answer = 1

while True:
    if answer > 1000:
        answer = -1
        break

    end = False
    
    for i in range(1, k+1):
        y, x, d = dic[i]
        if 0 > y+dy[d] or 0 > x+dx[d] or x+dx[d] >= n or y+dy[d] >= n or board[y+dy[d]][x+dx[d]] == 2:
            if d == 0 or d == 2:
                d += 1
            else:
                d -= 1

        ny = y + dy[d]
        nx = x + dx[d]
        if 0 > ny or 0 > nx or ny >= n or nx >= n or board[ny][nx] == 2:
            dic[i] = [y, x, d]
            continue

        elif board[ny][nx] == 0:
            dic[i][2] = d
            idx = mark[y][x].index(i)
            for j in range(idx, len(mark[y][x])):
                nd = dic[mark[y][x][j]][2]
                mark[ny][nx].append(mark[y][x][j])
                dic[mark[y][x][j]] = [ny, nx, nd]

            mark[y][x] = mark[y][x][:idx]

        else:
            dic[i][2] = d
            idx = mark[y][x].index(i)
            for j in range(len(mark[y][x])-1, idx-1, -1):
                nd = dic[mark[y][x][j]][2]
                mark[ny][nx].append(mark[y][x][j])
                dic[mark[y][x][j]] = [ny, nx, nd]

            mark[y][x] = mark[y][x][:idx]

        if len(mark[ny][nx]) >= 4:
            end = True
            break

    if end:
        break

    answer += 1

print(answer)

