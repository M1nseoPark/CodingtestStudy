import sys
sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().split())

adj = [[0] * (n + 1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    adj[a][b] = 1
    adj[b][a] = 1

visited = [False for _ in range(n+1)]

def dfs(v):
    visited[v] = True

    for i in range(1, n+1):
        if not visited[i] and adj[v][i] == 1:
            dfs(i)

answer = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        answer += 1

print(answer)
        
    
