import heapq

n = int(input())
minHeap = []

for _ in range(n):
    temp = list(map(int, input().split()))
    if len(minHeap) == 0:
        for i in range(n):
            heapq.heappush(minHeap, temp[i])
    else:
        for i in range(n):
            if minHeap[0] < temp[i]:
                heapq.heappush(minHeap, temp[i])
                heapq.heappop(minHeap)

print(minHeap[0])


