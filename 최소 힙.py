import heapq
import sys

n = int(sys.stdin.readline())
minHeap = []

for _ in range(n):
    x = int(sys.stdin.readline())

    if x != 0:
        heapq.heappush(minHeap, x)

    else:
        if len(minHeap) == 0:
            print(0)
        else:
            print(heapq.heappop(minHeap))
        
