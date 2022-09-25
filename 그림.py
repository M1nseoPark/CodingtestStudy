n, m = map(int, input().split())
draw = []
for _ in range(n):
    draw.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(y, x):
    global temp
    q = []
    q.append([y, x])
    draw[y][x] = 0

    while q:
        y, x = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and draw[ny][nx] == 1:
                q.append([ny, nx])
                draw[ny][nx] = 0
                temp += 1

temp = 1
answer = []
for i in range(n):
    for j in range(m):
        if draw[i][j] == 1:
            bfs(i, j)
            answer.append(temp)
            temp = 1

if len(answer) == 0:
    print(0)
    print(0)
else:
    print(len(answer))
    print(max(answer))
            
