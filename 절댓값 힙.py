import heapq
import sys

n = int(sys.stdin.readline())
minHeap = []

for _ in range(n):
    x = int(sys.stdin.readline())

    if x != 0:
        heapq.heappush(minHeap, [abs(x), x])

    else:
        if len(minHeap) == 0:
            print(0)
        else:
            temp = heapq.heappop(minHeap)
            print(temp[1])
        
        
        
    
    
