## 주사위는 숫자 기준이 아니라 방향 기준 -> 동서남북으로 굴렸을 때 인덱스 변화 저장
## 맞왜틀..
n, m, x, y, k = map(int, input().split())
maps = []
for _ in range(n):
    a1, a2 = map(int, input().split())
    maps.append([a1, a2])

dice = [0, 0, 0, 0, 0, 0]
order = list(map(int, input().split()))

dx = [1, -1, 0, 0]  # 동서북남
dy = [0, 0, -1, 1]

def turn(dir):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 0:  #동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c

    elif dir == 1:  #서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d

    elif dir == 2:  #북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b

    else:  # 남
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e


def roll(ny, nx, d):
    nx = nx + dx[d]
    ny = ny + dy[d]
    
    if 0 <= nx < m and 0 <= ny < n:
        turn(d)

        if maps[ny][nx] == 0:   # 0이면 주사위 바닥면에 쓰여 있는 수가 칸에 복사됨
            maps[ny][nx] = dice[-1]
        else:   # 0이 아니면 칸에 쓰여 있는 수가 주사위 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 됨
            dice[-1] = maps[ny][nx]
            maps[ny][nx] = 0

        print(dice[0])
        return ny, nx
    else:
        ox = nx - dx[d]
        oy = ny - dy[d]
        return oy, ox


for i in range(k):
    y, x = roll(y, x, order[i]-1)
