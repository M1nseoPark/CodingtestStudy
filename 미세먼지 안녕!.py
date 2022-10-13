# 공기청정기 이동을 처음에는 상하좌우 방향을 따로 계산해줬는데 이렇게 하면 꼭짓점 부분에서 문제가 생김
r, c, t = map(int, input().split())
board = []
for _ in range(r):
    board.append(list(map(int, input().split())))


clean = 0   # 공기청정기 위치
for i in range(r):
    if board[i][0] == -1:
        clean = i
        break

# 미세먼지 확산
def diffuse():
    dx = [1, 0, -1, 0]  # 시계 방향 (동북서남)
    dy = [0, -1, 0, 1]
    temp = [[0] * c for _ in range(r)]

    for y in range(r):
        for x in range(c):
            if board[y][x] != -1 and board[y][x] != 0:
                dust = board[y][x]
                # spread = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    # 칸이 없으면 확산이 일어나지 않음
                    if 0 > nx or 0 > ny or nx >= c or ny >= r:
                        continue

                    # 공기청정기가 있으면 확산이 일어나지 않음
                    if board[ny][nx] == -1:
                        continue

                    # spread += 1
                    temp[ny][nx] += dust // 5
                    temp[y][x] -= dust // 5

                # temp[y][x] += board[y][x] - ((dust // 5) * spread)

    for i in range(r):
        for j in range(c):
            board[i][j] += temp[i][j]


# 공기청정기 작동
def air_up():
    dx = [1, 0, -1, 0]  # 시계 방향 (동북서남)
    dy = [0, -1, 0, 1]

    d, before = 0, 0
    x, y = 1, clean
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        if y == clean and x == 0:   # 순환 후 공기청정기 위치에 도착하면
            break

        if nx < 0 or ny < 0 or nx >= c or ny >= r:   # 한쪽 방향의 끝에 도착하면
            d += 1
            continue

        board[y][x], before = before, board[y][x]
        y, x = ny, nx


def air_down():
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    d, before = 0, 0
    x, y = 1, clean + 1
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        if y == (clean + 1) and x == 0:
            break

        if nx < 0 or ny < 0 or nx >= c or ny >= r:
            d += 1
            continue

        board[y][x], before = before, board[y][x]
        y, x = ny, nx


for _ in range(t):
    diffuse()
    air_up()
    air_down()

answer = 0
for i in range(r):
    for j in range(c):
        answer += board[i][j]

print(answer + 2)   # 공기청정기 2개 -2
