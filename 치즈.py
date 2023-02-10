from collections import deque

r, c = map(int, input().split())
board = []
for _ in range(r):
    board.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def air(y, x):
    q = deque()
    q.append([y, x])

    while q:
        y, x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < c and 0 <= ny < r and board[ny][nx] == 0:
                board[ny][nx] = 2
                q.append([ny, nx])
                mq.append([ny, nx])

def melt():
    while mq:
        y, x = mq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < c and 0 <= ny < r and board[ny][nx] == 1:
                board[ny][nx] = 2


answer, day = 0, 0
while True:
    mq = deque()
    y, x = -1, -1
    cnt = 0
    
    for i in range(r):
        for j in range(c):
            if board[i][j] == 0 and (y == -1 and x == -1):
                y, x = i, j
            elif board[i][j] == 1:
                cnt += 1

    if cnt == 0:
        break
    else:
        answer = cnt
        day += 1
        
    air(y, x)
    melt()

    for i in range(r):
        for j in range(c):
            if board[i][j] == 2:
                board[i][j] = 0
                
        
print(day)
print(answer)
                
