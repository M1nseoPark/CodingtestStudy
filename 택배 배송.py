import heapq, sys

INF = sys.maxsize

def dijkstra(start):
    minHeap = []
    heapq.heappush(minHeap, [0, start])
    dist[start] = 0

    while minHeap:
        d, now = heapq.heappop(minHeap)

        if dist[now] != d:
            continue

        for i in graph[now]:
            cost = d + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(minHeap, [cost, i[0]])
                

n, m = map(int, input().split())
dist = [INF for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

dijkstra(1)
print(dist[n])
    

