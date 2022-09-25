n = int(input())
maps = []
for _ in range(n):
    maps.append(list(map(int, input())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(y, x):
    q = []
    q.append([y, x])
    maps[y][x] = 0
    count = 1

    while q:
        y, x = q.pop(0)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and maps[ny][nx] == 1:
                maps[ny][nx] = 0
                q.append([ny, nx])
                count += 1

    return count


answer = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            answer.append(bfs(i, j))

print(len(answer))
answer.sort()
for i in answer:
    print(i)
            
