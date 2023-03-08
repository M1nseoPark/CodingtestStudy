code = '0' + input()

# 1~26
dp = [0] * len(code)
if int(code[1]) == 0:
    print(0)
else:
    dp[0], dp[1] = 1, 1

    for i in range(2, len(code)+1):
        if 1 <= int(str(code[i-1])+str(code[i])) <= 26:
            dp[i] = (dp[i-1] + dp[i-2]) % 1000000
        else:
            dp[i] = dp[i-1] % 1000000

    print(dp[len(code)] % 1000000)
        
    
    
