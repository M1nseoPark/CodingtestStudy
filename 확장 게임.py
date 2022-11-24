# 한 방향으로 가는 게 아니라 다른 방향으로 꺾어서 이동할 수 있음 

from collections import deque

n, m, p = map(int, input().split())
arr = list(map(int, input().split()))
board = []
for _ in range(n):
    board.append(list(input()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def extend(idx):
    q = deque()

    for i in range(n):
        for j in range(m):
            if board[i][j] == str(idx):
                q.append([i, j])
  
    rst = False
    while q:
        y, x = q.popleft()

        for i in range(4):
            for j in range(1, arr[idx-1]+1):
                nx = x + (dx[i] * j)
                ny = y + (dy[i] * j)

                if 0 <= nx < m and 0 <= ny < n:
                    if board[ny][nx] == '.':
                        board[ny][nx] = str(idx)
                        rst = True

                    else:
                        for k in range(4):
                            nx = x + dx[
    
    return rst


while True:
    result = False
    for i in range(1, p+1):
        result = extend(i)
  
    if not result:
        break


    
answer = [0 for _ in range(p)]

for k in range(1, p+1):
    for i in range(n):
        for j in range(m):
            if board[i][j] == str(k):
                answer[k-1] += 1

print(' '.join(map(str, answer)))
