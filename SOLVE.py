import heapq

n = int(input())
m = int(input())
bus = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    bus[a].append([b, c])  # 도착점, 비용 
start, end = map(int, input().split())


def dijkstra(start):
    dist = [float('inf')] * (n + 1)
    prev = [0] * (n + 1)
    dist[start] = 0
    minHeap = []
    heapq.heappush(minHeap, [0, start])   # 비용, 위치 

    while minHeap:
        d, v = heapq.heappop(minHeap)

        if dist[v] != d:
            continue

        for i in bus[v]:
            cost = d + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                prev[i[0]] = v
                heapq.heappush(minHeap, [cost, i[0]])

    return dist, prev

dist, prev = dijkstra(start)
print(dist[end])
result = [end]
cur = end

while cur != start:
    result.append(prev[cur])
    cur = prev[cur]

result = result[::-1]
print(len(result))
print(' '.join(map(str, result)))



        

    
