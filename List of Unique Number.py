n = int(input())
arr = list(map(int, input().split()))

left, right = 0, 0
answer = 0
result = [arr[0]]
flag = True

while left < n and right < n:
    if flag:
        answer += 1
        right += 1
        if right < n:
            result.append(arr[right])
    else:
        left += 1

    
    
