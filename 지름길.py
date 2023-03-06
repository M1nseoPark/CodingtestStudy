import heapq, sys

n, k = map(int, input().split())
road = [[] for _ in range(k+1)]
for _ in range(n):
    a, b, c = map(int, input().split())
    if b <= k:
        road[a].append([b, c])

for i in range(k):
    road[i].append([i+1, 1])

INF = sys.maxsize
dist = [INF for _ in range(k+1)]

def dijkstra(start):
    minHeap = []
    heapq.heappush(minHeap, [0, start])
    dist[start] = 0

    while minHeap:
        d, now = heapq.heappop(minHeap)
        
        if dist[now] != d:
            continue

        for i in road[now]:
            cost = d + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(minHeap, [cost, i[0]])

dijkstra(0)
print(dist[k])
            
    
    
    

