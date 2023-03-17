import copy

sea = []
for _ in range(4):
    a, b, c, d, e, f, g, h = list(map(int, input().split()))
    sea.append([[a, b-1], [c, d-1], [e, f-1], [g, h-1]])

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

answer = 0

def dfs(sx, sy, score, sea):
    global answer

    score += sea[sx][sy][0]
    answer = max(answer, score)
    sea[sx][sy][0] = 0

    # 물고기 이동
    for f in range(1, 17):
        fx, fy = -1, -1
        for x in range(4):
            for y in range(4):
                if sea[x][y][0] == f:
                    fx, fy = x, y
                    break

        if fx == -1 and fy == -1:
            continue

        fd = sea[fx][fy][1]

        for i in range(8):
            nd = (fd + i) % 8
            nx = fx + dx[nd]
            ny = fy + dy[nd]

            if not (0 <= nx < 4 and 0 <= ny < 4) or (nx == sx and ny == sy):
                continue

            sea[fx][fy][1] = nd
            sea[fx][fy], sea[nx][ny] = sea[nx][ny], sea[fx][fy]
            break

    # 상어 먹음
    sd = sea[sx][sy][1]
    for i in range(1, 4):
        nx = sx + dx[sd]*i
        ny = sy + dy[sd]*i

        if 0 <= nx < 4 and 0 <= ny < 4 and sea[nx][ny][0] != 0:
            dfs(nx, ny, score, copy.deepcopy(sea))


dfs(0, 0, 0, sea)
print(answer)


            
            
                    
