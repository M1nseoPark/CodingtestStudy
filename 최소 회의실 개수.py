import heapq

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort()
heap = []
answer = 0

for i in range(n):
    while heap and heap[0] <= arr[i][0]:
        heapq.heappop(heap)

    heapq.heappush(heap, arr[i][1])
    answer = max(answer, len(heap))

print(answer)
        
