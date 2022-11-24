import sys

n = int(sys.stdin.readline())

dp = [i for i in range(n+1)]

idx = 2
i = idx ** 2

while i <= n:
    if i == (idx+1) ** 2:
        idx += 1
        
    for j in range(1, idx+1):
        dp[i] = min(dp[i], 1 + dp[i-j**2])
        
    i += 1

print(dp[n])
    
        


