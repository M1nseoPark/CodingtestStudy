from collections import deque

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    c = list(map(int, input().split()))
    tree[c[0]].append([c[1], c[2]])
    tree[c[1]].append([c[0], c[2]])


def bfs(start):
    visited = [-1] * (n + 1)
    visited[start] = 0
    q = deque()
    q.append(start)
    answer = [0, 0]

    while q:
        here = q.popleft()

        for e, w in tree[here]:
            if visited[e] == -1:
                visited[e] = visited[here] + w
                q.append(e)

                if answer[0] < visited[e]:
                    answer = [visited[e], e]

    return answer


dis, node = bfs(1)
dis, node = bfs(node)
print(dis)
            

