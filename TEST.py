from collections import deque

n = int(input())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def island(y, x):
    global idx

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


def bridge(d):
    global answer
    q = deque()
    visited = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if maps[i][j] == d:
                q.append([i, j])
                visited[i][j] = 1
                break

        if len(q) != 0:
            break

    while q:
        y, x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if maps[ny][nx] == d and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append([ny, nx])

                elif maps[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append([ny, nx])

                elif maps[ny][nx] != d and maps[ny][nx] != 0:
                    answer = min(answer, visited[y][x])
                    break
                


idx = 2
answer = n * n

for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            island(i, j)
            idx += 1


for i in range(2, idx):
    bridge(i)

print(answer)
    
                    


            

    
            
            


                

            
    
    




    
    
