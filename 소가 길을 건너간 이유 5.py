n, k, b = map(int, input().split())
arr = [0] * n

for _ in range(b):
    t = int(input())
    arr[t-1] = 1

left, right = 0, 0
temp = 0
if arr[left] == 1:
    temp += 1
answer = n+1

while left < n and right < n:
    if right - left + 1 == k:
        answer = min(answer, temp)

        if arr[left] == 1:
            temp -= 1
        left += 1

    else:
        right += 1

        if right < n:
            if arr[right] == 1:
                temp += 1

print(answer)
    
