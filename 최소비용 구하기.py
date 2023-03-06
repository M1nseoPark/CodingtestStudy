import heapq, sys

INF = sys.maxsize

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
bus = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    bus[a].append([b, c])

s, e = map(int, sys.stdin.readline().split())

def dijstra(start, end):
    dist = [INF] * (n + 1)
    dist[start] = 0
    minHeap = []
    heapq.heappush(minHeap, [0, start])

    while minHeap:
        d, now = heapq.heappop(minHeap)

        if dist[now] != d:
            continue

        for i in bus[now]:
            cost = d + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(minHeap, [cost, i[0]])

    return dist[end]


print(dijstra(s, e))
            
    
