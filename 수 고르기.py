n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()
left, right = 0, 1
answer = 2000000001

while left < n and right < n:
    temp = arr[right] - arr[left]
    if temp == m:
        answer = m
        break

    if temp < m:
        right += 1

    # left 0부터 시작했기 때문에 앞부분은 이미 확인했음
    else:
        left += 1
        answer = min(answer, temp)

print(answer)


            
        
        
