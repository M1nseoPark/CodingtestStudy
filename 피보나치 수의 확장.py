n = int(input())

if n == 0:
    print(0)
    print(0)
    
else:
    m = abs(n)
    dp = [0] * (m + 1)
    dp[1] = 1

    for i in range(2, m+1):
        dp[i] = dp[i-1] % 1000000000 + dp[i-2] % 1000000000

    if n < 0 and m % 2 == 0:
        print(-1)
    else:
        print(1)

    print(dp[m] % 1000000000)
    
        
    
    
