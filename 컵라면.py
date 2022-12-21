import heapq

n = int(input())
ramen = []
for _ in range(n):
    a, b = map(int, input().split())
    heapq.heappush(ramen, [a, -b])

answer = 0
time, i = 1, 0
solve = []

while ramen:
    if ramen[0][0] < time:
        heapq.heappop(ramen)

    else:
        temp = heapq.heappop(ramen)
        if temp[0] >= time:
            heapq.heappush(solve, temp[1])
        else:
            heapq.heappush(ramen, temp)
    else:
        if len(solve) != 0:
            answer += -solve[0]
        time += 1
        solve.clear()

if len(solve) != 0:
    answer += -solve[0]

print(answer)
    
        
        
    
        
    

