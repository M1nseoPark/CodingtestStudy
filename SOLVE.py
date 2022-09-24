import sys
sys.setrecursionlimit(10000)

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)

parent = [0] * (n + 1)
visited = [False for _ in range(n+1)]


def dfs(v):
    visited[v] = True
    
    for i in range(1, n+1):
        parent[tree[i][0]] = v
        visited[tree[i][0]] = True
        dfs(i)

dfs(1)
for i in range(2, n+1):
    print(parent[i])
    
    

    

            



        




    
