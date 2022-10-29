t = int(input())

dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1

def padovan(n):
    if dp[n] != 0:
        return dp[n]

    for i in range(1, n+1):
        if dp[i] == 0:
            dp[i] = dp[i-3] + dp[i-2]

    return dp[n]

            
for _ in range(t):
    n = int(input())
    print(padovan(n))

    
