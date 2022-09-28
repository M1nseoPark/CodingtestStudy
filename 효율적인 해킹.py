n, m = map(int, input().split())
abj = [[0] * (n + 1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    abj[a][b] = 1
    abj[b][a] = 1


visited = [False for _ in range(n+1)]
def bfs(v):
    q = []
    search = []
    q.append(v)
    search.append(v)
    visited[v] = True

    while q:
        here = q.pop()
        for i in range(1, n+1):
            if abj[here][i] == 1 and not visited[i]:
                q.append(i)
                visited[i] = True
                search.append(i)

    return search


answer = []
for i in range(1, n+1):
    if not visited[i]:
        answer.append(bfs(i))

print(answer)

    
        
    
