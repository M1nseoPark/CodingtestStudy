n = int(input())
m = int(input())

adj = [[0] * (n + 1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a][b] = 1
    adj[b][a] = 1

visited = [False for _ in range(n+1)]
answer = 0

def dfs(v):
    visited[v] = True
    global answer  # 전역변수 선언
    answer += 1

    for i in range(1, n+1):
        if not visited[i] and adj[v][i] == 1:
            dfs(i)

dfs(1)
print(answer - 1)
        
