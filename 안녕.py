n = int(input())
streng = [0] + list(map(int, input().split()))
happy = [0] + list(map(int, input().split()))

dp = [[0] * 101 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, 101):
        s = streng[i]
        h = happy[i]

        if s >= j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-s] + h)

print(dp[n][100])
