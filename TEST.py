n = int(input())
A = list(map(int, input().split()))

dp = [[0] * 2 for _ in range(n)]
for i in range(n):
    if A[i] < 0:
        dp[i][1] = max(dp[i-1][0], 0)
        dp[i][0] = max(dp[i-1][1] + A[i], dp[i-1][0] + A[i], A[i])
    else:
        dp[i][1] = dp[i-1][0] + A[i]
        dp[i][0] = max(dp[i-1][0], dp[i-1][1]) + A[i]

print(max(dp[n-1]))

