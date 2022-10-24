from collections import deque

n, k = map(int, input().split())

visited = [0] * 100001

def bfs(v):
    q = deque()
    q.append(v)

    while q:
        here = q.popleft()

        if here == k:
            print(visited[here])
            break

        for i in [here-1, here+1, here*2]:
            if 0 <= i <= 100000 and visited[i] == 0:
                visited[i] = visited[here] + 1
                q.append(i)
    
bfs(n)
    
    
