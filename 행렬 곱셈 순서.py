n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(n)]
for i in range(1, n):   # 몇 번째 대각선? 
    for j in range(n-i):   # 대각선에서 몇 번째 열?
        if i == 1:   # 차이가 1밖에 나지 않는 칸 
            dp[j][j+i] = arr[j][0] * arr[j][1] * arr[j+1][1]

        else:
            dp[j][j+1] = float('inf')
            for k in range(j, j+i):
                dp[j][j+i] = min(dp[j][j+i],
                                 dp[j][k]+dp[k+1][j+i]+arr[j][0]*arr[k][1]*arr[j+i][1])


print(dp[0][n-1])                

        
        
    
