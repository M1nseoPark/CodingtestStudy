import sys
sys.setrecursionlimit(10000000) 

n = int(input())
tree = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parents = [0] * (n + 1)
def dfs(start):
    for i in tree[start]:
        if parents[i] == 0:
            parents[i] = start
            dfs(i)


# 트리의 루트를 1이라고 정함 
dfs(1)

for i in range(2, n+1):
    print(parents[i])
    
    
