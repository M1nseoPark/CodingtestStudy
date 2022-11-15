# 짝수부터 시작하는게 아니라 처음부터 시작해야함!
# 마찬가지로 k번이 되면 다음 짝수번부터 시작하는게 아니라 left 1 증가 

n, k = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
idx, answer = 0, 0
temp = 1

if arr[left] % 2 == 1:
    idx += 1


while left < n and right < n:
    if idx > k:
        if arr[left] % 2 == 1:
            idx -= 1
        temp -= 1
        left += 1
        
    else:
        answer = max(answer, temp - idx)
        right += 1
        if right < n:
            if arr[right] % 2 == 1:
                idx += 1
            temp += 1

print(answer)

            
        
    
    
