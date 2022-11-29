from collections import deque

n = int(input())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

sy, sx, size = 0, 0, 2
for i in range(n):
    for j in range(n):
        if maps[i][j] == 9:
            sy, sx = i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
time = 0

def eat():
    q = deque()
    q.append([sy, sx])
    visited = [[-1] * n for _ in range(n)]
    visited[sy][sx] = 0
    fish = []   # 먹을 수 있는 물고기의 거리와 위치

    while q:
        y, x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == -1 and maps[ny][nx] <= size:
                q.append([ny, nx])
                visited[ny][nx] = visited[y][x] + 1
                if maps[ny][nx] != 0 and maps[ny][nx] < size:
                    fish.append([visited[ny][nx], ny, nx])

    # 거리가 가장 가까운 -> 가장 위에 있는 -> 가장 왼쪽에 있는 순서 
    fish.sort()
    return fish


temp = 0
while True:
    # 상어 위치에 따라 가까운 물고기도 달라지기 때문에 매번 탐색을 다시 해줘야 함 
    fish = eat()
    maps[sy][sx] = 0

    if len(fish) == 0:
        break

    t, y, x = fish[0][0], fish[0][1], fish[0][2]
    sy, sx = y, x

    temp += 1
    if temp == size:
        size += 1
        temp = 0

    time += t


print(time)
    
   
