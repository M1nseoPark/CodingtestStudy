from collections import deque

n, k = map(int, input().split())
arr = list(input())

rest, hun = deque(), deque()
answer = 0

for i in range(n):
    if arr[i] == 'H':
        rest.append(i)
        while hun:
            if i - hun[0] <= k:
                answer += 1
                rest.popleft()
                hun.popleft()
                break
            else:
                hun.popleft()
                
    else:
        while rest:
            if i - rest[0] > k:
                rest.popleft()
            else:
                break

        if rest:
            rest.popleft()
            answer += 1
        else:
            hun.append(i)

print(answer)
            
            
    
    
            
