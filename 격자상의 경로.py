n, m, k = map(int, input().split())

if k == 0:
    dp = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if i == 0:
                dp[i][j] = 1
            elif j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    print(dp[n-1][m-1])
    
else:
    cnt = 0
    y, x = -1, -1
    
    for i in range(n):
        for j in range(m):
            cnt += 1
            if cnt == k:
                y, x = i, j
                break
        if y != -1 and x != -1:
            break

    dp = [[0] * m for _ in range(n)]
    for i in range(y+1):
        for j in range(x+1):
            if i == 0:
                dp[i][j] = 1
            elif j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    for i in range(y, n):
        for j in range(x, m):
            if i == y and j == x:
                continue
            elif i == y:
                dp[i][j] = 1
            elif j == x:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    print(dp[y][x] * dp[n-1][m-1])
            
                
                
    
