import sys, heapq

INF = sys.maxsize

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
test = 1

def dijkstra():
    minHeap = []
    heapq.heappush(minHeap, [cave[0][0], 0, 0])
    dist[0][0] = cave[0][0]

    while minHeap:
        d, y, x = heapq.heappop(minHeap)

        if y == n - 1 and x == n - 1:
            print('Problem ' + str(test) + ': ' + str(dist[y][x]))
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                cost = d + cave[ny][nx]
                if cost < dist[ny][nx]:
                    dist[ny][nx] = cost
                    heapq.heappush(minHeap, [cost, ny, nx])
    

while True:
    n = int(input())

    if n == 0:
        break
    
    cave = []
    for i in range(n):
        cave.append(list(map(int, input().split())))

    dist = [[INF] * n for _ in range(n)]

    dijkstra()
    test += 1

    
