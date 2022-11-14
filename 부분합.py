import sys

n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

left, right = 0, 0
temp = arr[0]
answer = 100001

while left < n and right < n:
    if temp >= s:
        answer = min(answer, right - left + 1)
        temp -= arr[left]
        left += 1

    else:
        right += 1
        if right == n:
            break
        else:
            temp += arr[right]
        

if answer == 100001:
    print(0)
else:
    print(answer)

    
        
        
