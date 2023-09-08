def solution(n):
    if n % 2 == 1:
        return 0
    
    dp = [0, 3, 11]
    idx = n//2
    
    for i in range(3, idx+1):
        dp.append((3*dp[i-1] + 2*sum(dp[1:i-1]) + 2) % 1000000007)
    
    return dp[-1]