import heapq

def solution(operations):
    minHeap = []
    maxHeap = []
    exist = {}
    
    for i in operations:
        com = i.split()
        
        if com[0] == 'I':
            heapq.heappush(minHeap, int(com[1]))
            heapq.heappush(maxHeap, -int(com[1]))
            exist[int(com[1])] = 1
        
        else:
            if com[1] == '1':
                while maxHeap:
                    temp = heapq.heappop(maxHeap)
                    if exist[-temp] == 1:
                        exist[-temp] = 0
                        break
            
            else:
                while minHeap:
                    temp = heapq.heappop(minHeap)
                    if exist[temp] == 1:
                        exist[temp] = 0
                        break
    
    while maxHeap:
        temp = heapq.heappop(maxHeap)
        if exist[-temp] == 1:
            heapq.heappush(maxHeap, temp)
            break
    
    while minHeap:
        temp = heapq.heappop(minHeap)
        if exist[temp] == 1:
            heapq.heappush(minHeap, temp)
            break
    
    if len(minHeap) == 0 and len(maxHeap) == 0:
        answer = [0, 0]
    else:
        answer = [-maxHeap[0], minHeap[0]]
                        
    return answer
