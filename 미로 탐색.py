n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, input())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visited = [[0] * m for _ in range(n)]

def bfs(y, x):
    q = []
    q.append([y, x])
    visited[y][x] = 1

    while q:
        y, x = q.pop(0)

        if y == (n - 1) and x == (m - 1):
            break
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and maze[ny][nx] == 1 and visited[ny][nx] == 0:
                maze[ny][nx] = maze[y][x] + 1
                visited[ny][nx] = 1
                q.append([ny, nx])


bfs(0, 0)
print(maze[n-1][m-1])
                
    
