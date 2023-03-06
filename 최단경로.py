import heapq, sys

INF = sys.maxsize

v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])

dist = [INF] * (v + 1)


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

dijkstra(k)
for i in range(1, v+1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])




