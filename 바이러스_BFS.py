n = int(input())
m = int(input())

adj = [[0] * (n + 1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a][b] = 1
    adj[b][a] = 1

discovered = [0] * (n + 1)

def bfs(v):
    q = []
    q.append(v)
    discovered[v] = 1

    while len(q) != 0:
        here = q.pop(0)
        for i in range(1, n+1):
            if discovered[i] == 0 and adj[v][i] == 1:
                q.append(i)
                discovered[i] = 1
                print(discovered)

               
bfs(1)
print(sum(discovered) - 1)
            
    
    
