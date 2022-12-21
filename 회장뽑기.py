from collections import deque

n = int(input())
abj = [[0] * (n+1) for _ in range(n+1)]
while True:
    a, b = map(int, input().split())
    
    if a == -1 and b == -1:
        break
    
    abj[a][b] = 1
    abj[b][a] = 1

distance = [0 for _ in range(n+1)]
visited = [False for _ in range(n+1)]

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = True

    while q:
        here = q.popleft()

        for i in range(1, n+1):
            if not visited[i] and abj[here][i] == 1:
                q.append(i)
                visited[i] = True
                distance[i] = distance[here] + 1

    return max(distance)


cand = []                
for i in range(1, n+1):
    cand.append(bfs(i))
    visited = [False for _ in range(n+1)]
    distance = [0 for _ in range(n+1)]

score = min(cand)
answer = []
for i in range(n):
    if cand[i] == score:
        answer.append(i+1)

print(score, len(answer))
print(' '.join(map(str, answer)))
        



    
