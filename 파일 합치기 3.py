import heapq

t = int(input())
for _ in range(t):
    k = int(input())
    file = list(map(int, input().split()))

    minHeap = []
    for i in range(k):
        heapq.heappush(minHeap, file[i])

    answer = 0
    while len(minHeap) > 2:
        a = heapq.heappop(minHeap)
        b = heapq.heappop(minHeap)
        heapq.heappush(minHeap, a+b)
        answer += (a + b)

    answer += sum(minHeap)
    print(answer)

