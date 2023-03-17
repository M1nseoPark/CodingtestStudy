from collections import deque

n = int(input())
time = [0]
graph = [[] for _ in range(n+1)]
indegree = [0] * (n + 1)

for i in range(1, n+1):
    temp = list(map(int, input().split()))
    time.append(temp[0])
    for j in range(temp[1]):
        indegree[i] += 1
        graph[temp[j+2]].append(i)

result = [0] * (n + 1)
q = deque()

for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)
        result[i] = time[i]

while q:
    now = q.popleft()

    for i in graph[now]:
        indegree[i] -= 1
        result[i] = max(result[i], result[now] + time[i])
        
        if indegree[i] == 0:
            q.append(i)

print(max(result))
            



