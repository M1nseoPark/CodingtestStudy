def dfs(prev, node):
    visited[node] = True

    for i in tree[node]:
        if i == prev:
            continue
        if visited[i]:
            return False
        if not dfs(node, i):
            return False

    return True
    

test = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    tree = [[] for _ in range(n+1)]
    visited = [False] * (n + 1)
    for _ in range(m):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    cnt = 0   # 트리의 개수
    for v in range(1, n+1):   # 정점 번호 1~n
        if not visited[v]:   # 방문하지 않은 경우에만 DFS 수행 
            if dfs(0, v):
                cnt += 1   # 사이클이 없는 경우 트리 개수 증가

    if cnt > 1:
        print('Case '+str(test)+': A forest of '+str(cnt)+' trees.')
    elif cnt == 0:
        print('Case '+str(test)+': There is one tree.')
    else:
        print('Case '+str(test)+': No trees.')
    
