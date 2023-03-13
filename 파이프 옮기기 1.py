n = int(input())
home = []
for _ in range(n):
    home.append(list(map(int, input().split())))

dp = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]   # 가로, 세로, 대각선
dp[0][1][0] = 1

for i in range(2, n):
    if home[0][i] == 0:
        dp[0][i][0] += dp[0][i-1][0]


for i in range(1, n):
    for j in range(1, n):
        if home[i][j] == 0:
            dp[i][j][0] += (dp[i][j-1][0] + dp[i][j-1][2])
            dp[i][j][1] += (dp[i-1][j][1] + dp[i-1][j][2])

        if home[i][j] == 0 and home[i-1][j] == 0 and home[i][j-1] == 0:
            dp[i][j][2] += (dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2])


print(sum(dp[n-1][n-1]))
