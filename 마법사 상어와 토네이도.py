n = int(input())
sand = []
for _ in range(n):
    sand.append(list(map(int, input().split())))

wind = []
t = 1
while t < n:
    wind.append(t)
    wind.append(t)
    t += 1
wind.append(n)

# 이차원 배열 90도 회전하는 함수
def rotate(arr):
    new = list(reversed(list(zip(*arr))))
    return new


dx = [-1, 0, 1, 0]   # 서남동북
dy = [0, 1, 0, -1]
p = [[0, 0, 0.02, 0, 0],
     [0, 0.1, 0.07, 0.01, 0],
     [0.05, 0, 0, 0, 0],
     [0, 0.1, 0.07, 0.01, 0],
     [0, 0, 0.02, 0, 0]]
p1 = rotate(p)
p2 = rotate(p1)
p3 = rotate(p2)


def flutter(y, x, origin, dir):
    iy, ix = 0, 0
    stx, fix, sty, fiy = 0, 0, 0, 0

    if 0 <= y - 2:
        sty = y - 2
    if 0 <= x - 2:
        stx = x - 2
    if y + 3 < n:
        fiy = y + 3
    if x + 3 < n:
        fix = x + 3

    for i in range(st, y+3):
        ix = 0
        for j in range(x-2, x+3):
            sand[i][j] += origin * flu[dir][iy][ix]
            ix += 1
        iy += 1


d = 0
x, y = 0, 0
for w in wind:
    for i in range(w):
        y += dy[i]
        x += dx[i]
        origin = sand[y][x]
        flutter(y, x, origin, d)

    d = (d + 1) % 4

print('------')
for i in range(n):
    print(sand[i])
