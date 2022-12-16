import heapq
import sys

'''
I 3, I 7, I 3 입력 -> (3, 0), (7, 1), (3, 2)
D -1 입력 -> (3, 0) 삭제, visited[0] = 0
위의 결과에 따라 maxHeap도 정리를 해줘야 함 -> clear 함수 
'''
        
t = int(sys.stdin.readline())
for _ in range(t):
    k = int(sys.stdin.readline())
    minHeap = []
    maxHeap = []
    visited = [False] * k
    
    for i in range(k):
        a, b = sys.stdin.readline().split()
        if a == 'I':
            heapq.heappush(minHeap, [int(b), i])
            heapq.heappush(maxHeap, [-int(b), i])
            visited[i] = True

        else:
            # 최댓값 삭제
            if b == '1':   
                while maxHeap:
                    if visited[maxHeap[0][1]] == 0:
                        heapq.heappop(maxHeap)
                if maxHeap:
                    visited[maxHeap[0][1]] = False
                    heapq.heappop(maxHeap)
                
            # 최솟값 삭제 
            else:
                while minHeap:
                    if visited[minHeap[0][1]] == 0:
                        heapq.heappop(minHeap)
                if minHeap:
                    visited[minHeap[0][1]] = False
                    vheapq.heappop(minHeap)

    while minHeap:
        if visited[minHeap[0][1]] == 0:
            heapq.heappop(minHeap)
    while maxHeap:
        if visited[maxHeap[0][1]] == 0:
            heapq.heappop(maxHeap)
    
    if len(minHeap) == 0:
        print('EMPTY')
    else:
        print(-maxHeap[0][0], minHeap[0][0])

    
                
        
    
