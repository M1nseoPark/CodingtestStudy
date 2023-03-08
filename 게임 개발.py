from collections import deque

n = int(input())

indegree = [0] * (n + 1)
graph = [[] for _ in range(n+1)]
time = [0] * (n + 1)

for i in range(1, n+1):
    temp = list(map(int, input().split()))
    time[i] = temp[0]
    for j in range(1, len(temp)-1):
        graph[temp[j]].append(i)
        indegree[i] += 1

result = [0] * (n + 1)
q = deque()
price, b = [], 0

for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    result[now] += time[now]
    
    for i in graph[now]:
        indegree[i] -= 1
        result[i] = max(result[i], result[now])
        if indegree[i] == 0:
            q.append(i)

print(result)
    
