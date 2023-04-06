n, m, k = map(int, input().split())
board1 = [[[] for _ in range(n)] for _ in range(n)]   # 총 위치 
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] != 0:
            board1[i][j].append(temp[j])
board2 = [[0] * n for _ in range(n)]   # 플레이어 위치 

player = {}
for i in range(1, m+1):
    y, x, d, s = map(int, input().split())   
    player[i] = [y-1, x-1, d, s, 0]   # (y, x), 방향, 초기 능력치, 가지고 있는 총의 공격력 
    board2[y-1][x-1] = i

dy = [-1, 0, 1, 0]   # 상우하좌 
dx = [0, 1, 0, -1]
score = [0] * (m + 1)

def fight(wid, lid, y, x):
    # 진 플레이어가 본인이 가지고 있던 총을 격자에 내려놓음
    if player[lid][4] != 0:
        board1[y][x].append(player[lid][4])
    player[lid][4] = 0

    # 이긴 플레이어는 가장 공격력이 높은 총을 획득 
    if len(board1[y][x]) != 0 and player[wid][4] < max(board1[y][x]):
        board1[y][x].append(player[wid][4])
        ng = max(board1[y][x])
        board1[y][x].pop(board1[y][x].index(ng))
        player[wid][4] = ng

    # 진 플레이어 이동 
    for i in range(4):
        nd = (player[lid][2] + i) % 4
        ny = y + dy[nd]
        nx = x + dx[nd]

        if 0 <= ny < n and 0 <= nx < n and board2[ny][nx] == 0:
            # 이동하려는 칸에 총이 있다면 총 획득 
            if len(board1[ny][nx]) != 0:
                ng = max(board1[ny][nx])
                player[lid][4] = ng
                board1[ny][nx].pop(board1[ny][nx].index(ng))

            player[lid][0], player[lid][1], player[lid][2] = ny, nx, nd
            board2[ny][nx] = lid
            break
    
    # 이긴 플레이어 이동 
    player[wid][0], player[wid][1] = y, x
    board2[y][x] = wid


for _ in range(k):
    for i in range(1, m+1):
        y, x, d, s, g = player[i]
        ny = y + dy[d]
        nx = x + dx[d]

        if 0 > ny or 0 > nx or ny >= n or nx >= n:
            if d == 0 or d == 1:  d += 2
            else:  d -= 2
            ny = y + dy[d]
            nx = x + dx[d]
            player[i][2] = d   ## 빼먹음! 
        
        # 이동한 칸이 비어있을 경우 
        if len(board1[ny][nx]) == 0 and board2[ny][nx] == 0:
            player[i][0], player[i][1] = ny, nx
            board2[ny][nx], board2[y][x] = board2[y][x], board2[ny][nx]
        
        # 이동한 칸에 플레이어가 있을 경우 
        elif board2[ny][nx] != 0:
            foe = board2[ny][nx]
            board2[y][x] = 0
        
            if s + g > player[foe][3] + player[foe][4]:
                score[i] += (s + g) - (player[foe][3] + player[foe][4])
                fight(i, foe, ny, nx)

            elif s + g < player[foe][3] + player[foe][4]:
                score[foe] += (player[foe][3] + player[foe][4]) - (s + g)
                fight(foe, i, ny, nx)

            else:
                if s > player[foe][3]:
                    fight(i, foe, ny, nx)
                else:
                    fight(foe, i, ny, nx)

        # 이동한 칸에 총이 있을 경우 
        elif len(board1[ny][nx]) != 0:
            if g == 0:
                player[i][4] = max(board1[ny][nx])
                board1[ny][nx].pop(board1[ny][nx].index(player[i][4]))
            else:
                if g < max(board1[ny][nx]):
                    board1[ny][nx].append(g)
                    player[i][4] = max(board1[ny][nx])
                    board1[ny][nx].pop(board1[ny][nx].index(player[i][4]))
            
            player[i][0], player[i][1] = ny, nx
            board2[ny][nx], board2[y][x] = board2[y][x], board2[ny][nx]


print(score)
