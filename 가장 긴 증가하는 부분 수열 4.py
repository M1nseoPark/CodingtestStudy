n = int(input())
arr = list(map(int, input().split()))

dp = [[] for _ in range(n)]
for i in range(n):
    dp[i].append(arr[i])

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            if len(dp[j]) + 1 > len(dp[i]):
                dp[i] = dp[j] + [arr[i]]

answer = []
for i in range(n):
    if len(dp[i]) > len(answer):
        answer = dp[i]

answer.sort()
print(len(answer))
print(' '.join(map(str, answer)))
    
