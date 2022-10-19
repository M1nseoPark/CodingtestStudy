n = int(input())
A = list(map(int, input().split()))
x = int(input())

answer = 0
left = 0
right = n - 1
A.sort()

while left < right:
    if A[left] + A[right] == x:
        answer += 1
        left += 1
        right -= 1
        
    elif A[left] + A[right] > x:
        right -= 1
        
    else:
        left += 1
    
            
print(answer)
