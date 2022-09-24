import sys
sys.setrecursionlimit(10000)

n = int(input())
complex = []
for _ in range(n):
    complex.append(list(map(int, input())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(y, x):
    global temp
    complex[y][x] = 0
    temp += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and complex[ny][nx] == 1:
            complex[ny][nx] = 0
            dfs(ny, nx)


answer = []
temp = 0
for i in range(n):
    for j in range(n):
        if complex[i][j] == 1:
            dfs(i, j)
            answer.append(temp)
            temp = 0

print(len(answer))
answer.sort()
for i in answer:
    print(i)
