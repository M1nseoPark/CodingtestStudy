n, m = map(int, input().split())
floor = []
for _ in range(n):
    floor.append(list(input()))

visited = [[0] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(y, x):
    global answer
    visited[y][x] = 1

    if floor[y][x] == '-':
        for i in range(1):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 > nx or 0 > ny or nx <= n or ny <= n:
                continue

            if visited[ny][nx] == 1:
                continue

            if floor[ny][nx] == '|':
                answer += 1
                dfs(ny, nx)
            else:
                dfs(ny, nx)

    else:
        for i in range(2, 4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 > nx or 0 > ny or nx <= n or ny <= n:
                continue

            if visited[ny][nx] == 1:
                continue

            if floor[ny][nx] == '-':
                answer += 1
                dfs(ny, nx)
            else:
                dfs(ny, nx)

answer = 0
dfs(0, 0)
print(answer)
        
