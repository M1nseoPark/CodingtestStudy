n = int(input())
arr = list(map(int, input().split()))

left = 0
right = n-1
answer = 300000000

while left < right:
    temp = arr[left] + arr[right]
    if temp == 0:
        answer = 0
        break

    if answer > abs(temp):
        answer = temp
        left += 1

    else:
        right -= 1


print(answer)
        
