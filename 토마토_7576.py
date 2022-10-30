# BFS를 사용하여 최단거리를 구하는 문제

m, n = map(int, input().split())
tomato = []
for _ in range(n):
    tomato.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs():
    while q:
        y, x = q.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and tomato[ny][nx] == 0:
                q.append([ny, nx])
                tomato[ny][nx] = tomato[y][x] + 1


q = []
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append([i, j])  # 익은 토마토 큐에 저장


bfs()
answer = 0
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            print(-1)
            exit(0)   # 프로그램 종료

    answer = max(answer, max(tomato[i]))

print(answer - 1)

            
              
