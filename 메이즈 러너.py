import copy

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

n, m, k = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

entry = []
for _ in range(m):
    y, x = map(int, input().split())
    entry.append([y-1, x-1])

exit = list(map(int, input().split()))  # 출구의 좌표 
exit[0] -= 1
exit[1] -= 1
answer = 0   # 참가자들의 이동거리 합 

def find(exit, visit):
    start, end = [0, 0], [0, 0]
    flag = False

    for size in range(2, n):
        for sy in range(0, n-size+1):
            for sx in range(0, n-size+1):
                ey = sy + size - 1
                ex = sx + size - 1

                if sy <= exit[0] <= ey and sx <= exit[1] <= ex:
                    for y, x in visit:
                        if sy <= y <= ey and sx <= x <= ex:
                            start = [sy, sx]
                            end = [ey, ex]
                            flag = True
                            break
                if flag:
                    break
            if flag:
                break
        if flag:
            break
    
    return start[0], start[1], end[0], end[1]


answer = 0
for t in range(k):
    # 참가자 이동 
    visit = set()
    moved = []
    for y, x in entry:
        dist1 = abs(y-exit[0]) + abs(x-exit[1])  # 현재 머물러 있는 칸의 출구까지 거리
        flag = False   # 움직임 여부 표시 
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
        
            # 참가자는 벽이 없는 곳(빈칸 or 출구)으로 이동할 수 있다
            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == 0:
                dist2 = abs(ny-exit[0]) + abs(nx-exit[1])  # 움직인 칸의 출구까지의 거리
                if dist2 < dist1:  
                    # 이동한 칸이 출구가 아니라면 리스트에 추가해줌 
                    if not (ny == exit[0] and nx == exit[1]):
                        moved.append([ny, nx])
                        visit.add((ny, nx))
                    flag = True
                    break 
        
        # 움직일 수 없으면 움직이지 않음 
        if not flag:
            visit.add((y, x))
            moved.append([y, x])
        # 움직였다면 이동거리를 더해줌 
        else:
            answer += 1
    
    # 미로를 탈출했을 경우 
    if len(moved) == 0:
        break

    # 미로 회전 
    sy, sx, ey, ex = find(exit, visit)
    rotate = copy.deepcopy(board)
    m = ey - sy + 1
    
    for i in range(sy, ey+1):
        for j in range(sx, ex+1):
            oy, ox = i-sy, j-sx
            ry, rx = ox, m-oy-1
            if board[i][j] > 0:
                rotate[ry+sy][rx+sx] = board[i][j] - 1
            else:
                rotate[ry+sy][rx+sx] = board[i][j]
    
    for i in range(len(moved)):
        if sy <= moved[i][0] <= ey and sx <= moved[i][1] <= ex:
            oy, ox = moved[i][0]-sy, moved[i][1]-sx
            ry, rx = ox, m-oy-1
            moved[i] = [ry+sy, rx+sx]

    oy, ox = exit[0]-sy, exit[1]-sx
    ry, rx = ox, m-oy-1
    exit = [ry+sy, rx+sx]

    board = copy.deepcopy(rotate)
    entry = copy.deepcopy(moved)

print(answer)
print(exit[0]+1, exit[1]+1)