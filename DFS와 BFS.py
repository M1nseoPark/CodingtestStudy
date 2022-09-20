n, m, v = map(int, input().split())
adj = [[0] * (n + 1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a][b] = 1
    adj[b][a] = 1

visited = [False for _ in range(n+1)]

def dfs(v):
    visited[v] = True
    print(v, end=' ')

    for i in range(1, n+1):
        if (not visited[i]) and (adj[v][i] == 1):
            dfs(i)

def bfs(v):
    q = []
    q.append(v)
    print(v, end=' ')
    visited[v] = False

    while len(q) != 0:
        here = q.pop(0)
        for i in range(1, n+1):
            if visited[i] and (adj[here][i] == 1):
                q.append(i)
                visited[i] = False
                print(i, end=' ')

dfs(v)
print()
bfs(v)
