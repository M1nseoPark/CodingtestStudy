n, k = map(int, input().split())
arr = list(map(int, input().split()))

answer = n+1
kind = {}
kind[1] = 0
kind[2] = 0

left, right = 0, 0
kind[arr[0]] += 1

while left < n and right < n:
    if kind[1] >= k:
        answer = min(answer, right-left+1)
        kind[arr[left]] -= 1
        left += 1
    else:
        right += 1
        if right < n:
            kind[arr[right]] += 1

if answer == n+1:
    print(-1)
else:
    print(answer)
