# 문제를 착각했음, 같은 원소가 K개 이하

n, k = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
answer = 0
idx = {}

while True:
    right += 1

    if right < n:
        if max(idx.values()) < k:
            if arr[right] in arr[left:right]:
                idx += 1

        else:
            answer = max(answer, right - left)
            
            if arr[right] in arr[left:right]:
                if arr[left] == arr[right]:
                    idx -= 1
                else:
                    right -= 1

                left += 1

    else:
        break
    

print(answer)
        
        
    
