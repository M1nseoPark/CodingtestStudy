n = int(input())

arr = [i*i for i in range(1, int(n**0.5)+1)]
dp = [float('inf')] * (n + 1)
dp[0] = 0

for i in arr:
    for j in range(i, n+1):
        dp[j] = min(dp[j], dp[j-i]+1)

print(dp[n])
