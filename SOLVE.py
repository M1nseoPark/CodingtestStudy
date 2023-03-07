from collections import deque

n, m = map(int, input().split())
room = []
for _ in range(n):
    room.append(list(map(int, input().split())))

virus = []
for i in range(n):
    for j in range(n):
        if room[i][j] == 2:
            virus.append([i, j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(active):
    q = deque()
    visited = [[-1] * n for _ in range(n)]
    for i in range(len(active)):
        q.append(active[i])
        visited[active[i][0]][active[i][1]] = 0

    while q:
        y, x = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or 0 > ny or n <= nx or n <= ny:
                continue

            if visited[ny][nx] != -1:
                continue
            
            if room[ny][nx] == 0:
                visited[ny][nx] = visited[y][x] + 1
                q.append([ny, nx])
                
            if room[ny][nx] == 2:
                visited[ny][nx] = visited[y][x] + 1
                q.append([ny, nx])

    time = 0
    for i in range(n):
        for j in range(n):
            if room[i][j] == 0:
                if visited[i][j] == -1:
                    time = float('inf')
                    break
                else:
                    time = max(time, visited[i][j])
        if time == float('inf'):
            break

    return time
                    

def dfs(idx, active):
    global answer
    
    if idx == len(virus):
        return

    if len(active) == m:
        answer = min(answer, bfs(active))
        return

    dfs(idx+1, active+[virus[idx]])
    dfs(idx+1, active)


answer = float('inf')
dfs(0, [])
if answer == float('inf'):
    print(-1)
else:
    print(answer)
