n = int(input())
friend = [[0] * (n + 1) for _ in range(n+1)]

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    friend[a][b] = 1
    friend[b][a] = 1

visited = [False for _ in range(n+1)]
distance = [0 for _ in range(n+1)]

def bfs(v):
    visited[v] = True
    q = []
    q.append(v)

    while q:
        here = q.pop(0)
        
        for i in range(1, n+1):
            if not visited[i] and friend[here][i] == 1:
                q.append(i)
                visited[i] = True
                distance[i] = distance[here] + 1


bfs(1)
answer = 0
for i in range(n+1):
    if distance[i] != 0 and distance[i] <= 2:
        answer += 1

print(answer)
    
                
                
