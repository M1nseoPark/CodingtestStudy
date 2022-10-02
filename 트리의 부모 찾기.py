import sys
sys.setrecursionlimit(1000000)

n = int(input())
node = [[] for _ in range(n+1)]   # 인접 행렬로 풀면 메모리 초과

for i in range(n-1):
    a, b = map(int, input().split())
    node[a].append(b)   
    node[b].append(a)


def dfs(v):
    for i in node[v]:
        if parents[i] == 0:
            parents[i] = v
            dfs(i)


parents = [0] * (n + 1) 
dfs(1)

for i in range(2, n+1):
    print(parents[i])

    
