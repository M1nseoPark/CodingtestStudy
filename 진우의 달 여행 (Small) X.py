n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = [[[10000] * 3 for _ in range(m)] for _ in range(n)]

for i in range(m):
    for j in range(3):
        dp[0][i][j] = arr[0][i]

for i in range(1, n):
    for j in range(m):
        if j == 0:
            dp[i][j][0] = dp[i-1][j][1] + arr[i][j]
            dp[i][j][1] = dp[i-1][j+1][0] + arr[i][j]
        elif j == (m - 1):
            dp[i][j][1] = dp[i-1][j-1][2] + arr[i][j]
            dp[i][j][2] = dp[i-1][j][1] + arr[i][j]
        else:
            dp[i][j][0] = min(dp[i-1][j][1], dp[i-1][j-1][2]) + arr[i][j]
            dp[i][j][1] = min(dp[i-1][j+1][0], dp[i-1][j-1][2]) + arr[i][j]
            dp[i][j][2] = min(dp[i-1][j+1][0], dp[i-1][j][1]) + arr[i][j]

answer = 101 * n * m
for i in range(m):
    for j in range(3):
        answer = min(dp[n-1][i][j], answer)

for i in range(n):
    print(dp[i])
print(answer)
        
            
