n = int(input())

dp = [0] * (n + 1)
dp[0] = 4

for i in range(1, n+1):
    d = int(dp[i-1] ** 0.5)
    dp[i] = (d + d - 1) ** 2

print(dp[n])
