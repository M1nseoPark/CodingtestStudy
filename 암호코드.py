code = list(map(int, input()))
n = len(code)

dp = [0 for _ in range(n+1)]

if code[0] == 0:
    print(0)

else:
    code = [0] + code
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n+1):
        if code[i] > 0:
            dp[i] += dp[i-1]

        temp = code[i-1] * 10 + code[i]
        if temp >= 10 and temp <= 26:
            dp[i] += dp[i-2]

    print(dp[n] % 1000000)
