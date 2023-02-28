n, m = map(int, input().split())
ry, rx, d = map(int, input().split())
room = []
for _ in range(n):
    room.append(list(map(int, input().split())))

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def dfs(y, x, d):
    global answer

    if room[y][x] == 0:
        room[y][x] = 3
        answer += 1

    idx = 0
    flag = False
    ny, nx = 0, 0
    
    while idx != 4:
        d = (d - 1) % 4
        ny = y + dy[d]
        nx = x + dx[d]

        if 0 <= ny < n and 0 <= nx < m and room[ny][nx] == 0:
            flag = True
            break

        idx += 1

    if flag:
        dfs(ny, nx, d)
    else:
        if room[y-dy[d]][x-dx[d]] != 1:   # 후진 방향 실수해서 한참 헤맴!
            dfs(y-dy[d], x-dx[d], d)
        else:
            return

        
answer = 0
dfs(ry, rx, d)
print(answer)
    
