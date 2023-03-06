import heapq, sys

INF = sys.maxsize

n, e = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, sys.stdin.readline().split())


def dijkstra(start, end):
    minHeap = []
    heapq.heappush(minHeap, [0, start])
    dist = [INF] * (n + 1)
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

    return dist[end]


path1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
path2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)

if path1 >= INF and path2 >= INF:
    print(-1)
else:
    print(min(path1, path2))
                

