n = int(input())
stair = []
for _ in range(n):
    stair.append(int(input()))

dp = [0] * (n + 1)
dp[1] = stair[1]
dp[2] = stair[1] + stair[2]
dp[3] = max(stair[1] + stair[3], stair[2] + stair[3])

for i in range(4, n+1):
    dp[i] = max(dp[i-3] + stair[i-3] + stair[i-1],
                dp[i-3] + stair[i-2] + stair[i-1])

print(dp[n])
