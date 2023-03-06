n, x = map(int, input().split())
arr = list(map(int, input().split()))

ans, cnt = 0, 0
left, right = 0, 0
temp = arr[0]

while left < n and right < n:
    if right - left + 1 == x:
        if ans == temp:
            cnt += 1
        elif ans < temp:
            ans = temp
            cnt = 1

        temp -= arr[left]
        left += 1

    else:
        right += 1
        if right < n:
            temp += arr[right]

if ans == 0:
    print('SAD')
else:
    print(ans)
    print(cnt)
            
