# 시간 초과..
import sys
sys.setrecursionlimit(100000)

n = int(sys.stdin.readline())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

parent = [0] * (n + 1)
d = [-1] * (n + 1)

# 루트 노드부터 시작하여 깊이를 구하는 함수 
def dfs(now, depth):
    d[now] = depth

    for i in tree[now]:
        # 깊이를 이미 구한 경우 무시 
        if d[i] != -1:
            continue
        parent[i] = now
        dfs(i, depth+1)
    
dfs(1, 0)

def lca(a, b):
    # 두 노드의 깊이가 다를 경우 
    while d[a] != d[b]:
        # 깊이가 큰 노드가 부모 노드로 이동 
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]

    # 깊이는 같지만 두 노드가 서로 다를 경우 
    while a != b:
        # 두 노드를 부모 노드로 이동 
        a = parent[a]
        b = parent[b]

    return a


m = int(sys.stdin.readline())
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(lca(a, b))


