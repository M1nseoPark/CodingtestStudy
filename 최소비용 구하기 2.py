import heapq, sys

INF = sys.maxsize

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])

s, e = map(int, input().split())

dist = [INF] * (n + 1)
prev = [0] * (n + 1)   # 이전 노드 저장 -> end에서 이전 노드를 계속 거슬러가면 start가 나옴 


def dijkstra(start):
    dist[start] = 0
    minHeap = []
    heapq.heappush(minHeap, [0, start])

    while minHeap:
        d, now = heapq.heappop(minHeap)

        if dist[now] != d:
            continue

        for i in graph[now]:
            cost = d + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                prev[i[0]] = now
                heapq.heappush(minHeap, [cost, i[0]])


dijkstra(s)
print(dist[e])

path = [e]
now = e
while now != s:
    now = prev[now]
    path.append(now)

path.reverse()
print(len(path))
print(' '.join(map(str, path)))
    
