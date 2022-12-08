n, k = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
kt, answer = 0, 1

if arr[left] % 2 == 1:
    kt += 1
    answer = 0

while left < n-1 and right < n-1:
    if kt >= k:
        if arr[right+1] % 2 == 0:
            right += 1
        else:
            if arr[left] % 2 == 1:
                kt -= 1
            left += 1

    else:
        answer = max(right - left - kt + 1, answer)
        right += 1
        if arr[right] % 2 == 1:
            kt += 1




'''
1 12 123 
1 1  2

23 234 2345 
1  1   2
'''
    
    
    
        
