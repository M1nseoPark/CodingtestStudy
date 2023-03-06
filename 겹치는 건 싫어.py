n, k = map(int, input().split())
arr = list(map(int, input().split()))

kind = {}
answer = 0
kind[arr[0]] = 1

left, right = 0, 0
while left < n and right < n:
    if kind[arr[right]] > k:
        kind[arr[left]] -= 1
        left += 1

    else:
        answer = max(answer, right - left + 1)
            
        right += 1
        if right < n:
            if arr[right] in kind:
                kind[arr[right]] += 1
            else:
                kind[arr[right]] = 1
        
print(answer)
        
        
    
