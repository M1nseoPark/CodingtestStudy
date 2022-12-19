import heapq
import sys

n = int(sys.stdin.readline())
maxHeap = []

for _ in range(n):
    x = int(sys.stdin.readline())

    if x != 0:
        heapq.heappush(maxHeap, -x)

    else:
        if len(maxHeap) == 0:
            print(0)
        else:
            print(-heapq.heappop(maxHeap))
