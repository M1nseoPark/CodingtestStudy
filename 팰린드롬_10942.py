import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

dp = [[0] * n for _ in range(n)]
dp[0][0], dp[n-1][n-1] = 1, 1

for i in range(n-2, -1, -1):
    for j in range(i, n):
        if i == j:
            dp[i][j] = 1
        else:
            if A[i] == A[j] and j - i == 1:
                dp[i][j] = 1
            if A[i] == A[j] and dp[i+1][j-1] == 1:
                dp[i][j] = 1

m = int(sys.stdin.readline())
for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    s -= 1; e -= 1
    print(dp[s][e])

    

    

        
        

        
        
    
