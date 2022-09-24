import sys
sys.setrecursionlimit(10000)


m, n = map(int, sys.stdin.readline().split())
maps = []
for _ in range(m):
    maps.append(list(map(int, sys.stdin.readline().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(y, x):
    global answer
    
    if y == (m - 1) and x == (n - 1):
        answer += 1
        
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and maps[y][x] > maps[ny][nx]:
            dfs(ny, nx)

answer = 0
dfs(0, 0)
print(answer)



        




    
