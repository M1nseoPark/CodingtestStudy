import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

answer = 200000000
left = 0
right = n - 1

while answer != 0 and left < right:
    if abs(answer) > abs(arr[left]+arr[right]):
        answer = arr[left] + arr[right]

    if arr[left] + arr[right] > 0:
        right -= 1
    elif arr[left] + arr[right] < 0:
        left += 1

print(answer)

            
        
        
        
