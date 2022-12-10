import sys

n, m, k = map(int, sys.stdin.readline().split())
fire = []
for _ in range(m):
    yi, xi, mi, si, di = map(int, sys.stdin.readline().split())
    fire.append([yi-1, xi-1, mi, si, di])

maps = [[[] for _ in range(n)] for _ in range(n)]
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
move = 0


while move < k:
    # 파이어볼 이동
    for i in range(len(fire)):
        y, x, m, s, d = fire[i][0], fire[i][1], fire[i][2], fire[i][3], fire[i][4]
        for _ in range(s):
            x = (x + dx[d] + n) % n
            y = (y + dy[d] + n) % n
        maps[y][x].append([y, x, m, s, d])

    # 2개 이상의 파이어볼이 있는 칸에서는
    for i in range(n):
        for j in range(n):
            if len(maps[i][j]) >= 2:
                mass, speed = 0, 0
                fn = len(maps[i][j])
                flag = True
                rst = maps[i][j][0][4] % 2
                
                for f in range(fn):
                    mass += maps[i][j][f][2]
                    speed += maps[i][j][f][3]
                    if rst != (maps[i][j][f][4] % 2):
                        flag = False

                if mass // 5 == 0:
                    maps[i][j].clear()
                else:
                    maps[i][j].clear()
                    di = []
                    if flag:
                        di = [0, 2, 4, 6]
                    else:
                        di = [1, 3, 5, 7]

                    for f in range(4):
                        maps[i][j].append([i, j, mass//5, speed//fn, di[f]])    

    fire.clear()
    for i in range(n):
        for j in range(n):
            for f in range(len(maps[i][j])):
                fire.append(maps[i][j][f])

    move += 1
    maps = [[[] for _ in range(n)] for _ in range(n)]


answer = 0
for i in range(len(fire)):
    answer += fire[i][2]

print(answer)
    
    
