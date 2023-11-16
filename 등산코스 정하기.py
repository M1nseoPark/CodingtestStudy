import heapq

def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n+1)]
    for a, b, c in paths:
        graph[a].append([b, c])
        graph[b].append([a, c])
    
    is_summit = [False] * (n + 1)  #
    for summit in summits:
        is_summit[summit] = True
    
    def dijkstra():
        dist = [float('inf') for _ in range(n+1)]
        minHeap = []
        for gate in gates:  #
            dist[gate] = 0
            heapq.heappush(minHeap, [0, gate])
    
        while minHeap:
            d, now = heapq.heappop(minHeap)

            if dist[now] != d or is_summit[now]:
                continue

            for i in graph[now]:
                cost = max(i[1], d)

                if dist[i[0]] > cost:
                    dist[i[0]] = cost
                    heapq.heappush(minHeap, [cost, i[0]])
        
        return dist
    

    dist = dijkstra()
    answer = [-1, float('inf')]

    for summit in sorted(summits): #
        if dist[summit] < answer[1]:
            answer = [summit, dist[summit]]
    
    return answer


print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))