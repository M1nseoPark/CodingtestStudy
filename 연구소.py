# pypy로 풀어야 시간초과 안남

from collections import deque
import copy
import sys

n, m = map(int, sys.stdin.readline().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    global answer
    temp = copy.deepcopy(maps)
    q = deque()
    
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                q.append([i, j])
    
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and temp[ny][nx] == 0:
                temp[ny][nx] = 2
                q.append([ny, nx])

    result = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                result += 1

    answer = max(answer, result)


# 백트래킹 -> 이부분 코드 생각 못함
def makeWall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                maps[i][j] = 1
                makeWall(cnt+1)
                maps[i][j] = 0

answer = 0
makeWall(0)
print(answer)
        
        
        
    
