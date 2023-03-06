n, m = map(int, input().split())
read = [[0]]
for _ in range(m):
    read.append(list(map(int, input().split())))

dp = [[0] * (n + 1) for _ in range(m+1)]

for i in range(1, m+1):
    for j in range(1, n+1):
        d = read[i][0]
        p = read[i][1]

        if j < d:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-d] + p)

print(dp[m][n])
