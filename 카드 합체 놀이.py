import heapq

n, m = map(int, input().split())
card = list(map(int, input().split()))

heap = []
for i in range(n):
    heapq.heappush(heap, card[i])

for i in range(m):
    temp1 = heapq.heappop(heap)
    temp2 = heapq.heappop(heap)
    heapq.heappush(heap, temp1 + temp2)
    heapq.heappush(heap, temp1 + temp2)

print(sum(heap))
