# DFS로만 풀면 시간 초과
# 도착 지점까지 가는 경우의 수는 도착 지점이 아닌 임의의 점들에서 도착 지점까지 가는 경우의 수를 합한 것 

import sys
sys.setrecursionlimit(10000)


m, n = map(int, input().split())
height = []
for _ in range(m):
    height.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(y, x):
    if y == (m - 1) and x == (n - 1):
        return 1

    if visited[y][x] != -1:
        return visited[y][x]

    visited[y][x] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and height[y][x] > height[ny][nx]:
            visited[y][x] += dfs(ny, nx)

    return visited[y][x]


visited = [[-1] * n for _ in range(m)]
print(dfs(0, 0))
            
        
    
