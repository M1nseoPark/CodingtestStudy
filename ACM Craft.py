from collections import deque

test = int(input())
for _ in range(test):
    n, k = map(int, input().split())
    time = list(map(int, input().split()))
    
    graph = [[] for _ in range(n+1)]
    indegree = [0 for _ in range(n+1)]
    dp = [0 for _ in range(n+1)]
    q = deque()

    for i in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    w = int(input())

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = time[i-1]

    while q:
        now = q.popleft()

        for i in graph[now]:
            indegree[i] -= 1
            dp[i] = max(dp[i], dp[now] + time[i-1])
            if indegree[i] == 0:
                q.append(i)

    print(dp[w])
    
