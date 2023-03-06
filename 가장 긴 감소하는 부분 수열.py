n = int(input())
A = list(map(int, input().split()))

dp = [1] * n
for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
