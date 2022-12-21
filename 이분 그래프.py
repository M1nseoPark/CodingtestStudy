from collections import deque
import sys

k = int(sys.stdin.readline())

def bfs(v):
    q = deque()
    q.append(v)

    if visited[v] == 0:
        visited[v] = 1

    while q:
        here = q.popleft()
        color = visited[here]

        for i in graph[here]:
            if visited[i] == 0:   # 한 번도 방문하지 않은 정점이면 
                q.append(i)
                if color == 1:   # 현재의 정점과 다른 색깔로 지정 
                    visited[i] = 2
                else:
                    visited[i] = 1

            # 이미 방문했던 정점이면, 색이 같은지 확인 
            elif visited[i] == 1:
                if color == 1:
                    return False

            elif visited[i] == 2:
                if color == 2:
                    return False

    return True
                
    
for _ in range(k):
    v, e = map(int, sys.stdin.readline().split())
    graph = [[] for i in range(v+1)]
    visited = [0] * (v + 1)
    for i in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    result = True
    for i in range(1, v+1):
        result = bfs(i)
        if not result:
            break

    if result:
        print('YES')
    else:
        print('NO')
    

