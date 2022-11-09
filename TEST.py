from collections import deque

n = int(input())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def island(y, x):
    q = deque()
    q.append([y, x])
    maps[y][x] = idx

    while q:
        y, x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and maps[ny][nx] == 1:
                maps[ny][nx] = idx
                q.append([ny, nx])
    
    
idx = 2
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            island(i, j)
            idx += 1


def bridge(num):
    global answer
    q = deque()
    visited = [[-1] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if maps[i][j] == num:
                q.append([i, j])
                visited[i][j] = 0

    while q:
        y, x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == -1:
                if maps[ny][nx] == num:
                    q.append([ny, nx])
                    visited[ny][nx] = 0

                elif maps[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append([ny, nx])

                else:
                    answer = min(answer, visited[y][x])
                    return
                    
                
answer = n * n
for i in range(2, idx):
    bridge(i)

print(answer)
            
                

            
    
    




    
    
