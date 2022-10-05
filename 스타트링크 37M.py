from collections import deque
import sys

f, s, g, u, d = map(int, sys.stdin.readline().split())

visited = [-1] * (f + 1)

def bfs(v):
    q = deque()
    q.append(v)

    while q:
        here = q.popleft()

        if here == g:
            return visited[here] + 1
        
        if here + u <= f and visited[here+u] == -1:
            q.append(here + u)
            visited[here+u] = visited[here] + 1

        if here - d >= 1 and visited[here-d] == -1:
            q.append(here - d)
            visited[here-d] = visited[here] + 1


    return 'use the stairs'


if f == g or s == g:
    print(0)
else:
    print(bfs(s))
    
