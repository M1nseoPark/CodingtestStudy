import sys, heapq

INF = sys.maxsize

n, D = map(int, input().split())
road = [[] for _ in range(D+1)]
dist = [INF] * (D + 1)

# 이 부분을 생각 못함 
for i in range(D):
    road[i].append([i+1, 1])

for _ in range(n):
    a, b, c = map(int, input().split())
    if b <= D:
        road[a].append([b, c])

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
print(dist[D])
            
    
    
    

