v = int(input())
tree = [[] for _ in range(v+1)]
for i in range(v):
    a = list(map(int, input().split()))
    for j in range(1, len(a)-2, 2):
        tree[a[0]].append([a[j], a[j+1])


def bfs(start):
    visited = [-1 for _ in range(v+1)]
    q = deque()
    q.append(start)
    visited[start] = 0
    answer = [0, 0]

    while q:
        here = q.popleft()

        for e, w in tree[t]:
            if visited[here] == -1:
                visited[here] = visited[t] + w
                q.append(e)
                if answer[0] < visited[e]:
                    answer = visited[e], e
                    
    return answer
            

dis, node = bfs(1)
dis, node = bfs(node)
print(dis)
    

