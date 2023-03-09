import sys
sys.setrecursionlimit(1000000)

n, r, q = map(int, sys.stdin.readline().split())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

count = [0] * (n + 1)

def dfs(node):
    count[node] = 1
    for i in tree[node]:
        if count[i] == 0:
            dfs(i)
            count[node] += count[i]
            
dfs(r)
            
for _ in range(q):
    v = int(sys.stdin.readline())
    print(count[v])
        
