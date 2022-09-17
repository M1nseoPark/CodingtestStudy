# 우선순위 큐 안쓰면 메모리 초과
# 10과 20을 합친 뒤, 합친 30과 40을 합침
import heapq

n = int(input())
card = []
for _ in range(n):
    heapq.heappush(card, int(input()))

if len(card) == 1:
    print(0)
else:
    temp = 0
    while len(card) > 1:
        temp1 = heapq.heappop(card)
        temp2 = heapq.heappop(card)
        temp += temp1 + temp2
        heapq.heappush(card, temp1 + temp2)

    print(temp)
