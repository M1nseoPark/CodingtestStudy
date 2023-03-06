n, k = map(int, input().split())
c = [0] + list(map(int, input().split()))

dp = [[1000000] * (k + 1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][0] = 0

for i in range(1, n+1):
    for j in range(1, k+1):
        if j < c[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-c[i]] + 1)

if dp[n][k] == 1000000:
    print(-1)
else:
    print(dp[n][k])
