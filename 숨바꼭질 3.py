from collections import deque

n, k = map(int, input().split())

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = True

    while q:
        here = q.popleft()

        if here == k:
            return time[here]

        if 0 <= here * 2 <= 100000 and not visited[here*2]:
            time[2*here] = time[here]
            q.append(here*2)
            visited[here*2] = True

        for i in [here-1, here+1]:
            if 0 <= i <= 100000 and not visited[i]:
                time[i] = time[here] + 1
                q.append(i)
                visited[i] = True


visited = [0] * 100001
time = [0] * 100001

print(bfs(n))
            
                
