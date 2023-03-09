import sys
sys.setrecursionlimit(1000000)

test = int(input())

for _ in range(test):
    n = int(input())
    tree = [[] for _ in range(n+1)]
    parent = [0] * (n + 1)
    for i in range(n-1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
        parent[b] = a

    d = [-1] * (n + 1)

    def dfs(node, depth):
        d[node] = depth

        for i in tree[node]:
            if d[i] != -1:
                continue

            dfs(i, depth+1)

    root = -1
    for i in range(1, n+1):
        if parent[i] == 0:
            root = i
            break

    dfs(root, 0)

    def nca(a, b):
        while d[a] != d[b]:
            if d[a] > d[b]:
                a = parent[a]
            else:
                b = parent[b]

        while a != b:
            a = parent[a]
            b = parent[b]

        return a

    a, b = map(int, input().split())
    print(nca(a, b))
        
