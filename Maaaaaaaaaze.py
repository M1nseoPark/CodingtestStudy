from itertools import permutations
from collections import deque
import sys

maze = []
for i in range(5):
    temp = []
    for j in range(5):
        temp.append(list(map(int, sys.stdin.readline().split())))
    maze.append(temp)

dy = [0, 0, -1, 1, 0, 0]
dx = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
    
answer = 5 ** 4

# 시계방향으로 90도 돌리기
def rotate(arr):
    result = [[0] * 5 for _ in range(5)]

    for r in range(5):
        for c in range(5):
            result[c][4-r] = arr[r][c]

    return result


# 입구에서 출구로 도달하는 경로 찾기 
def bfs(temp):
    result = 5 ** 4

    if temp[0][0][0] == 1 and temp[4][4][4] == 1:
        q = deque()
        q.append([0, 0, 0])
        visited = [[[-1] * 5 for _ in range(5)] for _ in range(5)]
        visited[0][0][0] = 0

        while q:
            z, y, x = q.popleft()

            if z == 4 and y == 4 and x == 4:
                result = min(result, visited[z][y][x])
                break

            for i in range(6):
                nz = z + dz[i]
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= nz < 5 and 0 <= ny < 5 and 0 <= nx < 5:
                    if visited[nz][ny][nx] == -1 and temp[nz][ny][nx] == 1:
                        visited[nz][ny][nx] = visited[z][y][x] + 1
                        q.append([nz, ny, nx])

    return result
                        
            
# 미로 만드는 모든 경우 구하기
for p in list(permutations([0, 1, 2, 3, 4], 5)):
    temp = [maze[p[0]], maze[p[1]], maze[p[2]], maze[p[3]], maze[p[4]]]

    for a in range(4):
        temp[0] = rotate(temp[0])
        for b in range(4):
            temp[1] = rotate(temp[1])
            for c in range(4):
                temp[2] = rotate(temp[2])
                for d in range(4):
                    temp[3] = rotate(temp[3])
                    for e in range(4):
                        temp[4] = rotate(temp[4])

                        answer = min(answer, bfs(temp))


if answer == 5 ** 4:
    print(-1)
else:
    print(answer)
            
            

