# 시간, 메모리 제한 너무 빡빡함..

from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
abj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    abj[b].append(a)


def bfs(v):
    visited = [False for _ in range(n+1)]
    visited[v] = True
    result = 1
    q = deque([v])

    while q:
        here = q.popleft()
        for i in abj[here]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                result += 1

    return result
                

answer = []
hacking = 0
for i in range(1, n+1):
    temp = bfs(i)
    if temp > hacking:
        answer = [i]
        hacking = temp
    elif temp == hacking:
        answer.append(i)

for i in answer:
    print(i, end=' ')

    
        
    
