import sys

n = int(sys.stdin.readline())
consult = []
for _ in range(n):
    consult.append(list(map(int, sys.stdin.readline().split())))

dp = [0 for _ in range(n+1)]

for i in range(n-1, -1, -1):
    if i + consult[i][0] <= n:
        dp[i] = max(consult[i][1] + dp[i+consult[i][0]], dp[i+1])
    else:
        dp[i] = dp[i+1]

print(dp[0])
        
