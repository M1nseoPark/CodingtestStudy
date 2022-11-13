n = int(input())
arr = list(map(int, input().split()))

arr.sort()
answer = 0

# 먼저 어떤 수를 선택해준다는 걸 생각 못함
# 어떤 수 제외 리스트 만든 뒤, 투포인터 이용하기
for i in range(n):
    temp = arr[:i] + arr[i+1:]
    left = 0
    right = n - 2

    while left < right:
        t = temp[left] + temp[right]
        if t == arr[i]:
            answer += 1
            break

        if t < arr[i]:
            left += 1
        else:
            right -= 1

print(answer)
        
    
