n, m, k, c = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))   # 나무 1~~100, 빈칸 0, 벽 -1

dx = [-1, 0, 1, 0, -1, 1, -1, 1]
dy = [0, -1, 0, 1, -1, 1, 1, -1]
answer = 0

# 제초제 뿌릴 칸 선택 
def pick():
    killer = []
    for y in range(n):
        for x in range(n):
            if board[y][x] > 0:
                kill = board[y][x]
                for i in range(4, 8):
                    for j in range(1, k+1):
                        ny = y + dy[i] * j
                        nx = x + dx[i] * j

                        if 0 <= ny < n and 0 <= nx < n and board[ny][nx] > 0:
                            kill += board[ny][nx]
                        else:
                            break
                
                killer.append([kill, y, x])
            else:
                killer.append([0, y, x])
    
    killer.sort(key=lambda x:(-x[0], x[1], x[2]))
    return killer[0]


for _ in range(m):
    grow = []
    breed = []
    num = []
    killed = []

    # 나무 성장, 번식 
    for y in range(n):
        for x in range(n):
            if board[y][x] > 0:
                cnt1, cnt2 = 0, 0
                breed.append([])
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if 0 <= ny < n and 0 <= nx < n:
                        if board[ny][nx] > 0:
                            cnt1 += 1
                        if board[ny][nx] == 0:
                            breed[-1].append([ny, nx])
                            cnt2 += 1

                if cnt2 > 0:
                    num.append((board[y][x] + cnt1) // cnt2)
                else:
                    num.append(0)
                    
                if cnt1 > 0:
                    grow.append([y, x, cnt1])

    for g in grow:
        y, x, cnt = g[0], g[1], g[2]
        board[y][x] += cnt
    
    for i in range(len(breed)):
        if len(breed[i]) > 0:
            for b in breed[i]:
                y, x = b[0], b[1]
                board[y][x] += num[i]
    
    kd, ky, kx = pick()
    if kd != 0:
        killed.append([[ky, kx]])
        answer += board[ky][kx]
        board[ky][kx] = -2

        for i in range(4, 8):
            for j in range(1, k+1):
                ny = ky + dy[i] * j
                nx = kx + dx[i] * j

                if 0 <= ny < n and 0 <= nx < n:
                    if board[ny][nx] > 0:
                        answer += board[ny][nx]
                        board[ny][nx] = -2
                        killed[-1].append([ny, nx])
                    else:
                        board[ny][nx] = -2
                        killed[-1].append([ny, nx])
                        break
    else:
        killed.append([[ky, kx]])
        board[ky][kx] = -2
    
    if len(killed) > c:
        clean = killed.pop(0)
        for y, x in clean:
            board[y][x] = 0

print(answer)

