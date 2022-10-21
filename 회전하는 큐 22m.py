from collections import deque

n, m = map(int, input().split())
num = deque([map(int, input().split())])
data = deque([i for i in range(1, n+1)])

ans = 0
while len(num) > 0:
    idx = 0
    for i in range(n):
        if data[i] == num[0]:
            idx = i
            break
    
    while True:
        print(data)
        if num[0] == data[0]:
            data.popleft()
            num.popleft()
            break

        if idx <= (n - idx):
            data.append(data.popleft())
            ans += 1
        else:
            data.appendleft(data.pop())
            ans += 1

print(ans)
        
    
    
