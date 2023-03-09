n = int(input())
A = list(map(int, input().split()))

# dp[a][b] = 가능한 경우의 수(a번째까지의 수를 사용하여 b가 나올 수 있는)
dp = [[0] * 21 for _ in range(n)]

dp[0][arr[0]] += 1
for i in range(1, n-1):
    for j in range(21):
        if dp[i-1][j]:
            if j + A[i] <= 20:
                dp[i][j+A[i]] += dp[i-1][j]
            if j - A[i] >= 0:
                dp[i][j-A[i]] += dp[i-1][j]

print(dp[n-2][A[n-1]])


