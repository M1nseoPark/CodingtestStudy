import heapq

n = int(input())

lecture = []
for i in range(n):
    lecture.append(list(map(int, input().split())))

lecture.sort()

minHeap = []
heapq.heappush(minHeap, lecture[0][1])

for i in range(1, n):
    if lecture[i][0] < minHeap[0]:
        heapq.heappush(minHeap, lecture[i][1])
    else:
        heapq.heappop(minHeap)
        heapq.heappush(minHeap, lecture[i][1])

print(len(minHeap))
    
    

    
