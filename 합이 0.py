# 특정 1개의 원소를 선택 후, 투 포인터를 통해 세 원소의 합이 0인 경우 찾아서 더해주면 됨
# 대충 알고리즘은 맞았는데 어떻게 중복을 제거하는지 몰랐음

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
answer = 0

for i in range(n):   
    left = i + 1
    right = n - 1

    while left < right:
        temp = arr[left] + arr[right]
        # 점수 총합이 0인 경우, 같은 값이 있는 것에 대한 처리 필요
        if temp == arr[i] * -1:
            if arr[left] == arr[right]: 
                answer += right - left

            # 다른 경우 right 값에 대한 개수의 합???
            else:
                answer += 

        elif temp > arr[i] * -1:
            right -= 1

        else:
            left += 1
            
print(answer)
