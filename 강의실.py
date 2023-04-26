import heapq

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x:x[1])   # 시작 시간으로 오름차순 정렬

heap = []
answer = 0

for i in arr:
    while heap and heap[0] <= i[1]:   # 가장 일찍 끝나는 시간보다 시작시간이 크면 
        heapq.heappop(heap)   # 이 회의는 i번째 회의랑 동시에 진행할 수 있음 

    heapq.heappush(heap, i[2])   # i번째 회의의 끝나는 시간을 추가
    answer = max(answer, len(heap))

print(answer)
    
    



