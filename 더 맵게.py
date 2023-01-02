import heapq

def solution(scoville, K):
    minHeap = []
    for i in range(len(scoville)):
        heapq.heappush(minHeap, scoville[i])
    
    answer = 0
    flag = False
    while len(minHeap) >= 2:
        temp1 = heapq.heappop(minHeap)
        if temp1 >= K:
            flag = True
            break
        
        temp2 = heapq.heappop(minHeap)
        heapq.heappush(minHeap, temp1 + (temp2 * 2))
        answer += 1
    
    if minHeap:
        temp = heapq.heappop(minHeap)
        if temp >= K:
            flag = True
    
    if flag:
        return answer
    else:
        return -1
