n = int(input())
tree = [[] for _ in range(n+1)]
dp = [[0, 0] for _ in range(n+1)]  # dp[n][0]은 n이 어댑터일 경우, dp[n][1]은 n이 어댑터가 아닐 경우 
visited = [False] * (n + 1)

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


# 현재 노드가 어댑터가 될 것인지 
def dfs(node):
    visited[node] = True
    dp[node][0] = 1

    for i in tree[node]:
        if not visited[i]:
            dfs(i)
            dp[node][0] += min(dp[i][0], dp[i][1])   # 자식 노드들이 어댑터거나 아니거나
            dp[node][1] += dp[i][0]   # 모든 자식 노드들이 어댑터여야 함 


dfs(1)
answer = min(dp[1][0], dp[1][1])
print(answer)


    
    

