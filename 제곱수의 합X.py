n = int(input())

dp = [0] * ((int(n**0.5) + 1) ** 2 + 1)
dp[1] = 1
dp[2] = 2
dp[3] = 3
idx = 2

while idx * idx <= n:
    dp[idx*idx] = 1
    
    for i in range(idx*idx+1, (idx+1)*(idx+1)):
        dp[i] = dp[idx*idx] + dp[i-idx*idx]

    idx += 1

print(dp[n])
