n = int(input())
dp = [[0]]
for _ in range(n):
    dp.append([0] + list(map(int, input().split())))

for i in range(2, n+1):
    for j in range(1, i+1):
        if j == 1:
            dp[i][j] = dp[i-1][j]

        elif j == i:
            dp[i][j] = dp[i-1][i-1]

        else:
            dp[i][j] = max(dp[i-1][j] + dp[i][j], dp[i-1][j+1] + dp[i][j])

print(dp[n])
