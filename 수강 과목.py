n, k = map(int, input().split())
subject = [[0]]
for _ in range(k):
    subject.append(list(map(int, input().split())))

dp = [[0] * (n + 1) for _ in range(k+1)]

for i in range(1, k+1):
    for j in range(1, n+1):
        w = subject[i][0]
        t = subject[i][1]

        if t > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-t] + w)

print(dp[k][n])
