# 코드트리 메이즈러너 
# 빈칸, 벽(1~9 내구도, 내구도 0이 되면 빈칸이 됨), 출구(즉시 탈출)

## 참가자 이동 
# 1초마다 모든 참가자는 '동시'에 '한 칸'씩 상하좌우로 움직임 
# 움직인 칸은 현재 머물러 있던 칸보다 출구까지의 최단 거리(∣x1−x2∣+∣y1−y2∣)가 가까워야 함
# 움직일 수 있는 칸이 2개 이상이라면, 상하로 움직이는 것을 우선시
# 움직일 수 없으면 움직이지 않음 
# 한 칸에 2명 이상의 모험가가 있을 수 있음 

## 미로 회전 
# 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형을 잡음
# 가장 작은 크기를 갖는 정사각형이 2개 이상이라면, r좌표 적은 것 -> c좌표 적은 것 우선 
# 선택된 정사각형은 시계방향으로 90도 회전하며, 회전된 벽은 내구도가 1씩 깎임 
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

exit = list(map(int, input().split()))  # 출구의 좌표 -> 변함 
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
    
    return start, end


for _ in range(k):
    # 미로를 탈출했을 경우 
    if len(visit) == 1 and (exit[0], exit[1]) in visit:
        break

    # 참가자 이동 
    visit = set()
    moved = []
    for y, x in entry:
        dist1 = abs(y-ey) + abs(x-ex)
        flag = False

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            dist2 = abs(ny-ey) + abs(nx-ex)

            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == 0 and dist2 < dist1:
                if not (ny == ey and nx == ex):
                    moved.append([ny, nx])
                    visit.add((ny, nx))
                flag = True
                break 
        
        if not flag:
            visit.add((y, x))
            moved.append([y, x])
    
    # 미로 회전 
    start, end = find(exit, visit)
    for i in range(start[0], end[0]+1):
        for j in range(start[1], end[1]+1):