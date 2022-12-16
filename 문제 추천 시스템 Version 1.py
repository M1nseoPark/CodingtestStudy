# 이전에 추천 문제 리스트에 있던 문제 번호가 다른 난이도로 다시 들어올 수 있음
# -> visited 리스트에 True 처리해줬어도 힙은 그대로임 -> 힙에 같은 문제 번호가 2개 있게 됨 
import heapq
import sys

n = int(sys.stdin.readline())
minHeap = []
maxHeap = []
level = {}
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())  # 문제번호, 난이도 
    heapq.heappush(minHeap, [b, a])
    heapq.heappush(maxHeap, [-b, -a])
    level[a] = b

m = int(sys.stdin.readline())
for _ in range(m):
    command = list(sys.stdin.readline().split())

    # 문제 추가 
    if command[0] == 'add':
        heapq.heappush(minHeap, [int(command[2]), int(command[1])])
        heapq.heappush(maxHeap, [-int(command[2]), -int(command[1])])
        level[int(command[1])] = int(command[2])

    # 문제 제거 
    elif command[0] == 'solved':
        level[int(command[1])] = 0

    # 문제 출력 
    else:
        # 가장 어려운 문제 번호 출력 
        if command[1] == '1':
            '''
            while maxHeap and level[-maxHeap[0][1]] != -maxHeap[0][0]:
                    heapq.heappop(maxHeap)
            print(-maxHeap[0][1])
            '''    
            while maxHeap:
                temp = heapq.heappop(maxHeap)
                if level[-temp[1]] == -temp[0]:
                    print(-temp[1])
                    heapq.heappush(maxHeap, temp)
                    break
            
        # 가장 쉬운 문제 번호 출력
        else:
            '''
            while minHeap and level[minHeap[0][1]] != minHeap[0][0]:
                    heapq.heappop(minHeap)
            print(minHeap[0][1])
            '''
            while minHeap:
                temp = heapq.heappop(minHeap)
                if level[temp[1]] == temp[0]:
                    print(temp[1])
                    heapq.heappush(minHeap, temp)
                    break
            
    
