from collections import deque


n = int(input())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

sy, sx = 0, 0   # 아기 상어의 위치 
size = 2   # 아기 상어의 크기

for i in range(n):
    for j in range(n):
        if maps[i][j] == 9:
            sy, sx = i, j


# 나는 먹을 수 있는 물고기를 세는 함수, 거리 재는 함수를 따로 작성했는데,
# 먹을 수 있는 물고기의 위치와 거리를 BFS로 먼저 측정해 저장하는 게 효율적 
def bfs(sy, sx, ss):
    visited = [[-1] * n for _ in range(n)]

    q = deque()
    q.append([sy, sx])
    visited[sy][sx] = 0
    temp = []   # 먹을 수 있는 물고기의 위치와 거리 

    while q:
        y, x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == -1 and maps[ny][nx] <= ss:
                q.append([ny, nx])
                visited[ny][nx] = visited[y][x] + 1

                if maps[ny][nx] < ss and maps[ny][nx] != 0:
                    temp.append([ny, nx, visited[ny][nx]])

    # 거리가 가장 가까운 -> 가장 위에 있는 -> 가장 왼쪽에 있는 순서 
    return sorted(temp, key=lambda x: (x[2], x[0], x[1]), reverse=True)


cnt = 0   
answer = 0   
while True:
    # 상어 위치에 따라 가까운 물고기도 달라지기 때문에 매번 탐색을 다시 해줘야 함 
    eat = bfs(sy, sx, size)  

    if len(eat) == 0:
        break

    ny, nx, dist = eat.pop()

    answer += dist
    maps[sy][sx], maps[ny][nx] = 0, 0

    sy, sx = ny, nx
    cnt += 1

    if cnt == size:
        size += 1
        cnt = 0


print(answer)
    
    
