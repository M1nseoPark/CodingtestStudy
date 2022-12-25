def solution(n):
    dp = [0] * (n + 1)
    
    for i in range(1, n+1):
        s = i
        temp = s
        while temp <= n:
            dp[temp] += 1
            s += 1
            temp += s
            
    return dp[n]
