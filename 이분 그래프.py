# 인접한 정점이면 다른 색으로 칠함
# 이분 그래프는 BFS를 할 때 같은 레벨의 정점끼리는 같은 색으로 칠해짐

k = int(input())

for _ in range(k):
    v, e = map(int, input().split())
    graph = [[0] * v for i in range(v)]
    for i in range(e):
        u, v = map(int, input().split())
        graph[u][v] = 1
        graph[v][u] = 1

    
        
