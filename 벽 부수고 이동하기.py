# 백트래킹으로 풀면 시간 초과
# 굳이 벽을 하나씩 부술 필요 없이 벽 파괴 기회를 나타내는 변수를 사용하면 됨
# 벽 파괴 기회를 나타내기 위해 3차원 리스트 사용

from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
           

def bfs():
    q = deque()
    q.append([0, 0, 0])

    while q:
        y, x, z = q.popleft()

        if y == (n - 1) and x == (m - 1):
            answer.append(visited[y][x][z])
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                # 다음 이동할 곳이 벽이 아니고, 아직 한 번도 방문하지 않았다면
                if maps[ny][nx] == 0 and visited[ny][nx][z] == 0:
                    q.append([ny, nx, z])
                    visited[ny][nx][z] = visited[y][x][z] + 1

                # 다음 이동할 곳이 벽이고, 벽 파괴 기회를 사용하지 않은 경우
                elif maps[ny][nx] == 1 and z == 0:
                    q.append([ny, nx, 1])
                    visited[ny][nx][1] = visited[y][x][0] + 1
    
answer = []
bfs()

if len(answer) == 0:
    print(-1)
else:
    print(min(answer) + 1)


