# push로 삽입하고 정렬하는 것보다 우선순위큐 쓰는게 더 빠름
# 어떤 가방에 넣을 수 있는 보석을 모아두고 거기서 제일 비싼 보석 고르기
import heapq
import sys

n, k = map(int, sys.stdin.readline().split())
jewel = []
bag = []

for _ in range(n):
    heapq.heappush(jewel, list(map(int, sys.stdin.readline().split())))   # 가벼운 순서대로 힙에 저장

for _ in range(k):
    bag.append(int(sys.stdin.readline()))

bag.sort()

answer = 0
temp = []   # 가방에 담을 수 있는 보석 리스트
for i in range(len(bag)):
    while jewel and bag[i] >= jewel[0][0]:
        # temp 리스트에 담은 보석은 제거함(temp에 계속 남아 있으니까)
        heapq.heappush(temp, -heapq.heappop(jewel)[1])   # 가격만 넣음
    if temp:
        answer -= heapq.heappop(temp)
    elif not jewel:
        break

print(answer)
        
        
        
        
    
    


