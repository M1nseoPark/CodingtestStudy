n = int(input())
arr = list(map(int, input().split()))

left, right = 0, n - 1  # n-1로 설정하면 범위 넘어가는지 확인할 필요 없이 전개 가능 
result = abs(arr[0] + arr[n-1])
aleft, aright = left, right

while left < right:  ##
    temp = arr[left] + arr[right]

    if abs(temp) <= result:
        aleft, aright = left, right
        result = abs(temp)

        if result == 0:
            break

    if temp < 0:
        left += 1
    else:
        right -= 1


print(arr[aleft], arr[aright])
        
    
