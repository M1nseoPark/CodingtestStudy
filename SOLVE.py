from collections import deque
import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m, p = map(int, sys.stdin.readline().split())
arr = [0] + list(map(int, sys.stdin.readline().split()))
board = []
for _ in range(n):
    board.append(list(sys.stdin.readline()))

castle = [deque() for _ in range(p+1)]   # 플레이어별 성의 위치 
answer = [0] * (p + 1)   # 플레이어별 성의 개수

for i in range(n):
    for j in range(m):
        if board[i][j] != '.' and board[i][j] != '#':
            castle[int(board[i][j])].append([i, j])
            answer[int(board[i][j])] += 1


def finish():
    rst = 0
    for i in range(1, p+1):
        rst += len(temp[i])

    if rst == 0:
        return True

    return False
    

def expand(turn):
    global finish
    visited = [[-1] * m for _ in range(n)]
    q = deque()
    
    for y, x in castle[turn]:
        q.append([y, x])
        visited[y][x] = 0

    castle[turn].clear()  # 현재 차례 플레이어가 가진 성의 위치 큐에 저장하고 temp 리셋

    while q:
        y, x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue

            if visited[ny][nx] != -1 or board[ny][nx] != '.':
                continue

            visited[ny][nx] = visited[y][x] + 1

            if visited[ny][nx] < arr[turn]:
                q.append([ny, nx])

            castle[turn].append([ny, nx])
            board[ny][nx] = str(turn)
            answer[turn] += 1
            finish = False


turn = 1
finish = False
while not finish:
    if turn == p + 1:
        finish = True
        turn = 0

    expand(turn)

    turn += 1


print(' '.join(map(str, answer)))



    
