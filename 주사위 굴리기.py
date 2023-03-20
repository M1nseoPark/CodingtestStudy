## 주사위는 숫자 기준이 아니라 방향 기준 -> 동서남북으로 굴렸을 때 인덱스 변화 저장
## 놓여져 있는 곳의 좌표는 (x, y)이다 -> y, x 바꿔야함!!
n, m, x, y, k = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

command = list(map(int, input().split()))

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]
dice = [0, 0, 0, 0, 0, 0]

move = [[3, 1, 0, 5, 4, 2], [2, 1, 5, 0, 4, 3], [4, 0, 2, 3, 5, 1],
        [1, 5, 2, 3, 0, 4]]

for c in command:
    ny = y + dy[c-1]
    nx = x + dx[c-1]

    if 0 > ny or 0 > nx or ny >= m or nx >= n:
        continue

    s = move[c-1]
    dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[s[0]], dice[s[1]], dice[s[2]], dice[s[3]], dice[s[4]], dice[s[5]]
    
    if maps[nx][ny] == 0:
        maps[nx][ny] = dice[5]
    else:
        dice[5] = maps[nx][ny]
        maps[nx][ny] = 0

    print(dice[0])
    y, x = ny, nx

