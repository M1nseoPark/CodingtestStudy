n = int(input())

dp = [[0] * 10 for _ in range(n+1)]   # dp[자리수][맨앞에오는숫자]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]

        elif j == 9:   # 9 뒤엔 오직 숫자 8만 올 수 있음
            dp[i][j] = dp[i-1][8]

        else:   # 1~8은 뒤에 올 수 있는 숫자가 총 2종류
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] 

print(sum(dp[n]) % 1000000000)
    
