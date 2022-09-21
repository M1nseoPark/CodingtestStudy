import sys
sys.setrecursionlimit(10000)

n = int(input())
picture = []
for _ in range(n):
    picture.append(list(input()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

visited = [[0] * n for _ in range(n)]   # picture이 0과 1이 아니므로 편의상

def dfs(x, y):
    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < n and visited[nx][ny] == 0 and picture[x][y] == picture[nx][ny]:
            dfs(nx, ny)
            

answer1 = 0
answer2 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            answer1 += 1
            dfs(i, j)

# 적록색약 구현
for i in range(n):
    for j in range(n):
        if picture[i][j] == 'R':
            picture[i][j] = 'G'

visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            answer2 += 1
            dfs(i, j)

print(answer1, answer2)
        

        

