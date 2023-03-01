n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if i == 0:
            if j == 0:
                dp[i][j] = arr[i][j]
            else:
                dp[i][j] = max(dp[i][j-1]+arr[i][j], dp[i][j]+arr[i][j])

        elif j == 0:
            dp[i][j] = max(dp[i-1][j]+arr[i][j], dp[i][j]+arr[i][j])

        else:
            dp[i][j] = max(dp[i-1][j]+arr[i][j], dp[i][j-1]+arr[i][j], dp[i-1][j-1]+arr[i][j])

print(dp[n-1][m-1])
                
        
            
