n = int(input())
A = list(map(int, input().split()))

dp = [float('inf')] * n
dp[0] = 0

for i in range(n):
    for j in range(i+1, i+A[i]+1):
        if j >= n:
            break
        dp[j] = min(dp[j], dp[i]+1)

if dp[n-1] == float('inf'):
    print(-1)
else:
    print(dp[n-1])
        
