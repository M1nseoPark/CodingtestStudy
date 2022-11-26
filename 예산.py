n = int(input())
arr = list(map(int, input().split()))
m = int(input())

left = 0   # min(arr)로 하면 틀림!!
right = max(arr)
answer = 0

while left <= right:
    mid = (left + right) // 2
    temp = []
        
    for i in range(n):
        if arr[i] > mid:
            temp.append(mid)
        else:
            temp.append(arr[i])

    if sum(temp) == m:
        answer = max(temp)
        break

    elif sum(temp) > m:
        right = mid - 1

    else:
        answer = max(temp)
        left = mid + 1

print(answer)
