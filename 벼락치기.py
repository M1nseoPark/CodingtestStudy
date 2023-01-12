n, t = map(int, input().split())
study = [[0]]
for _ in range(n):
    study.append(list(map(int, input().split())))

dp = [[0] * (t + 1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, t+1):
        k = study[i][0]
        s = study[i][1]

        if k > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-k] + s)

print(dp[n][t])
