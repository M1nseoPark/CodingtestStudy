n = int(input())
home = []
for _ in range(n):
    home.append(list(map(int, input().split())))

dy = [0, 1, 1]   # 가로, 대각선, 세로 
dx = [1, 1, 0]
visited = [[[-1] * 3 for _ in range(n)] for _ in range(n)]

def dfs(y, x, d):
    if visited[y][x][d] != -1:
        return visited[y][x][d]

    if y == (n - 1) and x == (n - 1):
        return 1

    visited[y][x][d] = 0
    print(y, x, d)

    if d == 0:
        for i in [0, 1]:
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and home[ny][nx] == 0:
                visited[y][x][d] += dfs(ny, nx, i)

    if d == 2:
        for i in [1, 2]:
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and home[ny][nx] == 0:
                visited[y][x][d] += dfs(ny, nx, i)

    if d == 1:
        for i in [0, 1, 2]:
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and home[ny][nx] == 0:
                visited[y][x][d] += dfs(ny, nx, i)

    return visited[y][x][d]


dfs(0, 1, 0)
print(visited)
        
