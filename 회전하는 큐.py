from collections import deque

n, m = map(int, input().split())
arr = list(map(int, input().split()))

dq = deque([i for i in range(1, n+1)])
ans = 0

for i in arr:
    while True:
        if dq[0] == i:
            dq.popleft()
            break

        if dq.index(i) <= len(dq)//2:
            dq.append(dq.popleft())
            ans += 1
        else:
            dq.appendleft(dq.pop())
            ans += 1

print(ans)
        
    
    
