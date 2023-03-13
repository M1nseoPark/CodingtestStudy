n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(n)]

for size in range(1, n):   # 분할된 그룹의 크기 
    for start in range(n-size):   # 크기 size인 그룹의 모든 경우의 수
        end = start + size

        rst = float('inf')
        for cut in range(start, end):
            rst = min(rst, dp[start][cut]+dp[cut+1][end]+
                      arr[start][0]*arr[cut][1]*arr[end][1])
        dp[start][end] = rst


print(dp[0][n-1])

# size=1, start=0~n-2
# size=2, start=0~n-3


        
        
    
