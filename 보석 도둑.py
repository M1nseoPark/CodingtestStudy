import heapq
import sys

n, k = map(int, sys.stdin.readline().split())
jewel = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    heapq.heappush(jewel, [a, -b])

bag = []
for _ in range(k):
    bag.append(int(sys.stdin.readline()))

bag.sort()
steal = []
answer = 0

for i in range(k):
    while jewel:
        temp = heapq.heappop(jewel)
        if bag[i] >= temp[0]:
            heapq.heappush(steal, temp[1])
        else:
            heapq.heappush(jewel, temp)
            break

    if len(steal) != 0:
        answer += -heapq.heappop(steal)

print(answer)
        
        
        
    
