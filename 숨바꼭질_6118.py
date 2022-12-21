from collections import deque

n, m = map(int, input().split())
abj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    abj[a].append(b)
    abj[b].append(a)

distance = [0 for _ in range(n+1)]


def bfs(v):
    q = deque()
    q.append(v)
    distance[v] = 1

    while q:
        here = q.popleft()

        for i in abj[here]:
            if distance[i] == 0:
                q.append(i)
                distance[i] = distance[here] + 1

bfs(1)
answer = []
score = max(distance)

for i in range(1, n+1):
    if distance[i] == score:
        answer.append(i)

print(answer[0], score-1, len(answer))
        
    
