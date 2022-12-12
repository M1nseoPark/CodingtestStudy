from collections import deque

n, m, k = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, input())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

answer = n * m

def bfs():
    global answer
    q = deque()
    q.append([0, 0, 0, 0])  # 낮은 0, 밤은 1
    visited = [[[[0] * 2 for _ in range(2)] for _ in range(m)] for _ in range(n)]
    visited[0][0][0][0] = 1

    while q:
        y, x, b, d = q.popleft()

        if y == n - 1 and x == m - 1:
            answer = min(answer, visited[y][x][b][d])
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if d == 0:  # 낮
                    if maps[ny][nx] == 0 and visited[ny][nx][b][1] == 0:
                        visited[ny][nx][b][1] = visited[y][x][b][0] + 1
                        q.append([ny, nx, b, 1])

                    elif maps[ny][nx] == 1 and b < k and visited[ny][nx][b+1][1] == 0:
                        visited[ny][nx][b+1][1] = visited[y][x][b][0] + 1
                        q.append([ny, nx, b+1, 1])

                else:  # 밤
                    if maps[ny][nx] == 0 and visited[ny][nx][b][0] == 0:
                        visited[ny][nx][b][0] = visited[y][x][b][1] + 1
                        q.append([ny, nx, b, 0])

                    elif maps[ny][nx] == 1 and b < k:
                        visited[y][x][b][0] = visited[y][x][b][1] + 1
                        q.append([y, x, b, 0])


bfs()
if answer == n * m:
    print(-1)
else:
    print(answer)
                        
                    
                
                
                
