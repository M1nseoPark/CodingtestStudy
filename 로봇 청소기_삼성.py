from collections import deque

n, m = map(int, input().split())
r, c, d = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

q = deque()
q.append([r, c])
visited = [[0] * m for _ in range(n)]
visited[r][c] = 1   # 현재 위치를 청소함

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
answer = 1

def bfs():
    global d, answer

    while q:
        y, x = q.popleft()
        clean = False
        for i in range(4):
            d = (d - 1) % 4   # 왼쪽 방향으로 회전
            nx = x + dx[d]  # 한 칸을 전진
            ny = y + dy[d]
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 0 and visited[ny][nx] == 0:
                q.append([ny, nx])
                answer += 1
                visited[ny][nx] = 1   # 현재 위치를 청소
                clean = True
                break
            else:
                continue

        # 네 방향 모두 청소가 이미 되어있거나 벽인 경우,
        if not clean:
            nx = x - dx[d]
            ny = y - dy[d]
            # 후진을 하고 2번으로 돌아감
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 0:
                q.append([ny, nx])
            # 후진도 할 수 없는 경우에는 작동을 멈춤
            else:
                return

bfs()
print(answer)
    
