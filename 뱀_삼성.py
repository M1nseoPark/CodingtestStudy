from collections import deque

n = int(input())
k = int(input())
board = [[0] * n for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1

move = deque()
l = int(input())
for _ in range(l):
    move.append(list(input().split()))

pos = deque()   # 뱀의 위치
pos.append([0, 0])
board[0][0] = 2
d, t = 1, 1   # 뱀의 방향, 시간

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

while True:
    nx = pos[-1][1] + dx[d]
    ny = pos[-1][0] + dy[d]

    # 뱀이 벽과 부딪치면 게임 끝남 
    if 0 > nx or 0 > ny or nx >= n or ny >= n:
        break

    # 뱀이 자기자신과 부딪치면 게임 끝남 
    if board[ny][nx] == 2:
        break

    if board[ny][nx] == 0:   # 이동한 칸에 사과가 없다면
        sy, sx = pos.popleft()
        board[sy][sx] = 0

    pos.append([ny, nx])
    board[ny][nx] = 2

    # 방향 전환 
    if len(move) != 0 and int(move[0][0]) == t:
        x, c = move.popleft()
        if c == 'L':
            d = (d + 3) % 4
        else:
            d = (d + 1) % 4

    t += 1

print(t)
