k = int(input())

dp = [[0, 0] for _ in range(46)]
dp[0] = [1, 0]
dp[1] = [0, 1]

for i in range(2, k+1):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]

print(dp[k][0], dp[k][1])
