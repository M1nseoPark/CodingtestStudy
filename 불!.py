r, c = map(int, input().split())
maze = []
for _ in range(r):
    maze.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

fvisited = [[0] * c for _ in range(r)]
svisited = [[0] * c for _ in range(r)]
fq = []

def fbfs():
    while fq:
        y, x = fq.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < c and 0 <= ny < r and maze[ny][nx] != '#' and fvisited[ny][nx] == 0:
                fvisited[ny][nx] = fvisited[y][x] + 1
                fq.append([ny, nx])


def sbfs(y, x):
    q = []
    q.append([y, x])
    svisited[y][x] = 1
    result = 0

    while q:
        y, x = q.pop(0)

        if y == 0 or y == (r - 1) or x == 0 or x == (c - 1):
            result = svisited[y][x]
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < c and 0 <= ny < r:
                if maze[ny][nx] != '#' and svisited[ny][nx] == 0:
                    if fvisited[ny][nx] == 0 or fvisited[ny][nx] > (svisited[y][x] + 1):
                        svisited[ny][nx] = svisited[y][x] + 1
                        q.append([ny, nx])

    return result


answer = 0

# 이것때매 엄청 틀림!!!
# 불은 여러 개일수도 있기 때문에 큐에 미리 넣어줘야 함
for i in range(r):
    for j in range(c):
        if maze[i][j] == 'F':
            fq.append([i, j])
            fvisited[i][j] = 1

fbfs()

for i in range(r):
    for j in range(c):
        if maze[i][j] == 'J':
            answer = sbfs(i, j)

if answer != 0:
    print(answer)
else:
    print('IMPOSSIBLE')
            
                
