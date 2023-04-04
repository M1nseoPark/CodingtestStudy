from collections import deque

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))   # 못 지나가는 칸 2로 하겠음!!!!

camp = {}   # 들어갈 수 있는 베이스캠프 위치 
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            camp[(i, j)] = 1

con = {}
for i in range(m):
    y, x = map(int, input().split())
    con[i] = (y-1, x-1)
time = 0

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]
cur = {}   # 각 사람의 현재 위치 

# 1) 한 칸 이동 
def move(num, fy, fx):
    sy, sx = cur[num]
    q = deque()
    q.append([fy, fx])
    dist = [[float('inf')] * n for _ in range(n)]
    dist[fy][fx] = 0

    while q:
        y, x = q.popleft()

        if y == sy and x == sx:
            break

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and dist[ny][nx] == float('inf') and board[ny][nx] != 2:
                dist[ny][nx] = dist[y][x] + 1
                q.append([ny, nx])
    
    return dist


# 3) 들어갈 베이스캠프 고르기 
def pick(num):
    fy, fx = con[num]
    result = []

    for key, val in camp.items():
        sy, sx = key
        q = deque()
        q.append([sy, sx])
        dist = [[-1] * n for _ in range(n)]
        dist[sy][sx] = 0

        while q:
            y, x = q.popleft()

            if y == fy and x == fx:
                result.append([dist[y][x], sy, sx])

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= ny < n and 0 <= nx < n and dist[ny][nx] == -1 and board[ny][nx] != 2:
                    dist[ny][nx] = dist[y][x] + 1
                    q.append([ny, nx])
    
    result.sort()
    return (result[0][1], result[0][2])


while True:
    dele = []

    for key, val in cur.items():
        dist = move(key, con[key][0], con[key][1])   # 인덱스, 사람의 현재 위치 (y, x)
        my, mx, d = -1, -1, float('inf')
        for i in range(4):
            ny = val[0] + dy[i]
            nx = val[1] + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if dist[ny][nx] < d:
                    d = dist[ny][nx]
                    my, mx = ny, nx
        
        if my == con[key][0] and mx == con[key][1]:
            dele.append(key)
            board[con[key][0]][con[key][1]] = 2
        else:
            cur[key] = [my, mx]
    
    for i in dele:
        del cur[i]

    if time < m:
        y, x = pick(time)
        del camp[(y, x)]
        board[y][x] = 2
        cur[time] = [y, x]

    if len(cur) == 0:
        break

    time += 1

print(time + 1)
