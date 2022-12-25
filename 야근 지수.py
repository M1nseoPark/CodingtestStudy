import heapq

def solution(n, works):
    maxHeap = []
    for i in range(len(works)):
        heapq.heappush(maxHeap, -works[i])
    
    for i in range(n):
        temp = heapq.heappop(maxHeap)
        if temp == 0:
            break
        heapq.heappush(maxHeap, temp+1)
    
    answer = 0
    for i in range(len(maxHeap)):
        answer += (maxHeap[i] * maxHeap[i])
        
    return answer
