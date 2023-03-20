# nxm, x=r, y=c
# 1번에 쓰여져 있는 값 출력
# 주사위 지도 바깥으로 이동시키려 하는 경우 명령 무시

n, m, x, y, k = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
arr = list(map(int, input().split()))
dice = [0 for _ in range(6)]

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

def roll(dir):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]

    if dir == 0:  # 원래의 0은 어디로 가는가 
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
    if dir == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    if dir == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e
    if dir == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b


for i in range(k):
    d = arr[i] - 1

    if 0 <= y + dy[d] < m and 0 <= x + dx[d] < n:
        y += dy[d]
        x += dx[d]
        roll(d)

        if board[x][y] == 0:
            board[x][y] = dice[5]
        else:
            dice[5] = board[x][y]
            board[x][y] = 0

        print(dice[0])
            

