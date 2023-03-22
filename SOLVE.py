sea = []
for _ in range(4):
    a, b, c, d, e, f, g, h = map(int, input().split())
    sea.append([[a, b-1], [c, d-1], [e, f-1], [g, h-1]])

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

dic = {}
for i in range(4):
    for j in range(4):
        dic[sea[i][j][0]] = [i, j, sea[i][j][1]]

sy, sx, sd = 0, 0, sea[0][0][1]
answer = sea[0][0][0]
del sea[0][0][0]
sea[0][0] = [0, 0]

while True:
    for i in range(1, 17):
        if i in dic:
            y, x, d = dic[i]

            for _ in range(8):
                ny = y + dy[d]
                nx = x + dx[d]

                if 0 > ny or 0 > nx or ny >= 4 or nx >= 4 or (sy == ny and sx == nx):
                    d = (d + 1) % 8
                    continue

                if sea[ny][nx][0] != 0:
                    cy, cx, cd = dic[sea[ny][nx][0]]
                    sea[y][x] = [sea[ny][nx][0], sea[ny][nx][1]]
                    sea[ny][nx] = [i, d]
                    dic[sea[y][x][0]] = [ny, nx, 
                    

                sea[y][x] = []


    
