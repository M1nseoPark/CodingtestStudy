import heapq, sys

n = int(sys.stdin.readline())

leftHeap = []   # 최대힙 
rightHeap = []   # 최소힙 

for _ in range(n):
    x = int(sys.stdin.readline())

    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, -x)
    else:
        heapq.heappush(rightHeap, x)

    # 1 2 순서로 들어왔을 경우 -> left=[-2], right=[1]
    if rightHeap and rightHeap[0] < -leftHeap[0]:
        left = heapq.heappop(leftHeap)
        right = heapq.heappop(rightHeap)

        heapq.heappush(leftHeap, -right)
        heapq.heappush(rightHeap, -left)

    print(-leftHeap[0])
        
        
