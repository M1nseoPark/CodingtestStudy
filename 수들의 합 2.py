import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

left, right = 0, 0
answer = 0
temp = arr[0]

while left < n and right < n:
    if temp == m:
        answer += 1
        temp -= arr[left]
        left += 1
        
    elif temp < m:
        right += 1
        if right < n:
            temp += arr[right]
        
    else:
        temp -= arr[left]
        left += 1

print(answer)
        
    
    
