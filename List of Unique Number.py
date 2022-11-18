n = int(input())
arr = list(map(int, input().split()))

left, right = 0, 1
answer = 1

while True:
    if right < n:
        if arr[right] not in arr[left:right]:
            answer += 1
            right += 1
        else:
            left += 1

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5


dp = [0 for _ in range(n)]
q = deque()
current = set()  # 현재 리스트 상태 

for i in range(n):
    if arr[i] in current:   # 현재 리스트에 이미 존재하는 원소일 경우 1 / 1 2
        while q:
            pos, value = q.popleft()
            current.remove(value)
            if value == arr[i]:
                break
            
    q.append([i, arr[i]])
    current.add(arr[i])

    dp[i] = len(current)


print(sum(dp))
