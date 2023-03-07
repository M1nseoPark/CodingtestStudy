import sys
sys.setrecursionlimit(1000000)

n = int(input())
boo = []
for _ in range(n):
    boo.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dp = [[0] * n for _ in range(n)]

def dfs(y, x):
    if dp[y][x] != 0:
        return dp[y][x]

    dp[y][x] = 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < n and boo[y][x] < boo[ny][nx]:
            dp[y][x] = max(dp[y][x], dfs(ny, nx)+1)

    return dp[y][x]

answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j))

print(answer)
        
    
