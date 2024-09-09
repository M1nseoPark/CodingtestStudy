from collections import deque

indegree = [0] * (v + 1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

answer = []
q = deque()

for i in range(1, v+1):
    if indegree[i] == 0:
        q.append(i)
        result[i] = time[i]

    while q:
        now = q.popleft()
        answer.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)