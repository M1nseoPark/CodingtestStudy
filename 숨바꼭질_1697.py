n, k = map(int, input().split())

visited = [0 for _ in range(10**5+1)]   # 최대는 2*k가 아니라 100000
def bfs(v):
    q = []
    q.append(v)

    while q:
        here = q.pop(0)

        if here == k:
            break

        for nv in (here - 1, here + 1, here * 2):
            if 0 <= nv <= 10 ** 5 and visited[nv] == 0:
                q.append(nv)
                visited[nv] = visited[here] + 1

bfs(n)
print(visited[k])
