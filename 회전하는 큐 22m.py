from collections import deque

n, m = map(int, input().split())
arr = list(map(int, input().split()))
deque = deque([i for i in range(1, n+1)])

ans = 0
for i in arr:
    while True:
        if num[0] == i:
            deque.popleft()
            break

        if deque.index(i) <= (n - idx):
            data.append(data.pop(0))
            ans += 1
        else:
            data = [data[-1]] + data[:-1]
            ans += 1

print(ans)
        
    
    
