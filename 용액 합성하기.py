n = int(input())
arr = list(map(int, input().split()))

left = 0
right = n - 1
answer = 30000000

while left < right:
    temp = arr[left] + arr[right]

    if temp == 0:
        answer = 0
        break

    elif temp < 0:
        if abs(answer) > abs(temp):
            answer = temp
        left += 1

    else:
        if abs(answer) > abs(temp):
            answer = temp
        right -= 1

print(answer)
        
