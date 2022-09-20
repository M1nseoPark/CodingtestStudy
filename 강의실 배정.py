import heapq

n = int(input())
room = []
for _ in range(n):
    room.append(list(map(int, input().split())))

fHeap = []
for i in range(n):
    heapq.heappush(fHeap, [room[i][1], room[i][0]])

answer = 0
eHeap = [fHeap[0]]
for i in range(1, n):
    if fHeap[i][0] > f

    
