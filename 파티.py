import sys, heapq

INF = sys.maxsize

n, m, x = map(int, sys.stdin.readline().split())
time = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    time[a].append([b, c])


def dijkstra(start):
    dist = [INF] * (n+1)
    minHeap = []
    dist[start] = 0
    heapq.heappush(minHeap, [0, start])

    while minHeap:
        d, now = heapq.heappop(minHeap)

        if dist[now] != d:
            continue

        for i in time[now]:
            cost = d + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(minHeap, [cost, i[0]])

    return dist


answer = 0
temp, dest = [], []
for i in range(1, n+1):
    dist = dijkstra(i)
    if i == x:
        dest = dist[1:]
        temp.append(dist[x])
    else:
        temp.append(dist[x])


for i in range(n):
    if answer < temp[i] + dest[i]:
        answer = temp[i] + dest[i]

print(answer)
    
        

