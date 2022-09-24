import sys
sys.setrecursionlimit(10000)

n = int(input())
a, b = map(int, input().split())
m = int(input())
family = [[0] * (n + 1) for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    family[x][y] = 1
    family[y][x] = 1

visited = [False for _ in range(n+1)]

def dfs(v, t):
    t += 1
    visited[v] = True

    if v == b:
        answer.append(t)
        

    for i in range(1, n+1):
        if (not visited[i]) and family[v][i] == 1:
            dfs(i, t)

answer = []
dfs(a, 0)

if len(answer) == 0:
    print(-1)
else:
    print(answer[0] - 1)
    
