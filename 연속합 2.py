n = int(input())
A = list(map(int, input().split()))

dp = [[0] * n for _ in range(2)]
dp[0][0] = A[0]
dp[1][0] = -1001   # 수는 한 개 이상 선택해야 하므로 불가능한 조건임 

for i in range(1, n):
    dp[0][i] = max(dp[0][i-1] + A[i], A[i]) 
    dp[1][i] = max(dp[0][i-1], dp[1][i-1] + A[i])

print(max(max(dp[0]), max(dp[1])))
            

    
            
    
