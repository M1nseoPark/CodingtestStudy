test = int(input())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def fbfs(y, x):
    q = []
    q.append([y, x])
    fvisited[y][x] = 1
    visited[y][x] = 1

    while q:
        y, x = q.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < w and 0 <= ny < h and maps[ny][nx] == '.' and fvisited[ny][nx] == 0:
                fvisited[ny][nx] = fvisited[y][x] + 1

                if visited[ny][nx] != 0:
                    visited[ny][nx] = min(fvisited[ny][nx], visited[ny][nx])
                else:
                    visited[ny][nx] = fvisited[ny][nx]

                q.append([ny, nx])


def sbfs(y, x):
    q = []
    q.append([y, x])
    svisited[y][x] = 1
    result = 0

    while q:
        y, x = q.pop(0)

        if y == 0 or y == (h - 1) or x == 0 or x == (w - 1):
            result = svisited[y][x]
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < w and 0 <= ny < h and maps[ny][nx] == '.':
                if svisited[ny][nx] == 0 and (visited[ny][nx] == 0 or visited[ny][nx] > (svisited[y][x] + 1)):
                    svisited[ny][nx] = svisited[y][x] + 1
                    q.append([ny, nx])

    return result
                
    

for _ in range(test):
    w, h = map(int, input().split())
    maps = []
    answer = 0

    visited = [[0] * w for _ in range(h)]
    svisited = [[0] * w for _ in range(h)]
    
    for i in range(h):
        maps.append(list(input()))

    for i in range(h):
        for j in range(w):
            if maps[i][j] == '*':
                fvisited = [[0] * w for _ in range(h)]
                fbfs(i, j)

    for i in range(h):
        for j in range(w):
            if maps[i][j] == '@':
                answer = sbfs(i, j)

    for i in range(h):
        print(visited[i])
    print('-----')
    for i in range(h):
        print(svisited[i])

    if answer != 0:
        print(answer)
    else:
        print('IMPOSSIBLE')
    

    

    
