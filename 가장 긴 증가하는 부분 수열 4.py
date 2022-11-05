# 나는 max문을 if문으로 구현하고 해당되는 경우마다 append를 해서 배열을 구했는데
# 왜 안되는지 모르겠음

n = int(input())
arr = list(map(int, input().split()))

dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
x = max(dp)

## 역추적
answer = []
for i in range(n-1, -1, -1):
    if dp[i] == x:
        answer.append(arr[i])
        x -= 1

answer.reverse()
print(' '.join(map(str, answer)))

    
