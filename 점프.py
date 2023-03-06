n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dx = [1, 0]
dy = [0, 1]
visited = [[-1] * n for _ in range(n)]

def dfs(y, x):
    if visited[y][x] != -1:
        return visited[y][x]
    
    if y == (n - 1) and x == (n - 1):
        return 1

    visited[y][x] = 0

    for i in range(2):
        nx = x + (dx[i] * board[y][x])
        ny = y + (dy[i] * board[y][x])

        if 0 <= nx < n and 0 <= ny < n:
            visited[y][x] += dfs(ny, nx)

    return visited[y][x]


print(dfs(0, 0))

    
        
