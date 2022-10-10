## 와 구현이 2시간이 걸리다니...
## 일단 다른사람 풀이 보고 넘어가고 나중에 다시 풀어보자
r, c, m = map(int, input().split())
shark = []
for _ in range(m):
    shark.append(list(map(int, input().split())))  # 상어 위치 x,y, 속력, 방향, 크기

# 상어 보드에 놓기
board = [[-1] * c for _ in range(r)]
for i in range(m):
    board[shark[i][0]-1][shark[i][1]-1] = i


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 상어 이동
def move(y, x, id):
    # y=0, x=2, id=1 -> 1 3 5 2 9
    board[y][x] = -1
    mo = shark[id][2]  # 상어가 이동할 칸 수
    di = shark[id][3] - 1

    for i in range(mo):
        if y + dy[di] < 0:
            di -= 1
        elif y + dy[di] >= r:
            di += 1
        elif x + dx[di] < 0:
            di -= 1
        elif x + dx[di] >= c:
            di += 1

        y += dy[di]
        x += dx[di]

    if board[y][x] != -1:
        if shark[id][4] > shark[board[y][x]][4]:
            board[y][x] = id

    for i in range(r):
        print(board[i])
    print('--3--')


# 상어 찾기
def pick():
    for i in range(r):
        for i in range(r):
            print(board[i])
        print('--2--')

        for j in range(c):
            if board[i][j] != -1:
                id = board[i][j]
                move(i, j, id)


# 낚시왕 상어 잡기
answer = 0
for i in range(c):
    # 1초 마다
    for j in range(r):
        if board[j][i] != -1:
            answer += shark[board[j][i]][4]
            board[j][i] = -1   # 낚시왕 상어 잡음
            break

    pick()


print(answer)
