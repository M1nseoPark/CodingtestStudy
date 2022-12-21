from collections import deque
import sys

n = int(sys.stdin.readline())
adj = []
for _ in range(n):
    adj.append(list(map(int, sys.stdin.readline().split())))

visited = [0 for _ in range(n)]

def bfs(v):
    q = deque()
    q.append(v)

    while q:
        here = q.popleft()

        for i in range(n):
            if visited[i] == 0 and adj[here][i] == 1:
                visited[i] = 1
                q.append(i)

    return visited


for i in range(n):
    temp = bfs(i)
    print(' '.join(map(str, temp)))
    visited = [0 for _ in range(n)]
    
    
    
    
