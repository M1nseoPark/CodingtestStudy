n = int(input())
A = list(map(int, input().split()))

dp = [[0] * 2 for _ in range(n)]

dp[0][0] = A[0]
dp[0][1] = -1001

for i in range(1, n):
    dp[i][0] = max(dp[i-1][0] + A[i], A[i])
    dp[i][1] = max(dp[i-1][0], dp[i-1][1] + A[i])

print(dp)

