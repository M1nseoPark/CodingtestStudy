# 0 → ─, 1 → /, 2 → |

n = int(input())
home = []
for _ in range(n):
    home.append(list(map(int, input().split())))
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]   # (y, x, 방향)

def solution():
    # 첫번째 행 처리하기 -> 항상 가로 파이프만 올 수 있음 
    dp[0][1][0] = 1
    for i in range(2, n):
        if home[0][i] == 0:   
            dp[0][i][0] = dp[0][i-1][0]

    for i in range(1, n):
        for j in range(1, n):
            # 대각선 파이프 추가 
            if home[i][j] == 0 and home[i][j-1] == 0 and home[i-1][j] == 0:
                dp[i][j][1] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]
            
            # 가로, 세로 파이프 추가
            if home[i][j] == 0:
                dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][1]
                dp[i][j][2] = dp[i-1][j][2] + dp[i-1][j][1]

    print(sum(dp[n-1][n-1][i] for i in range(3)))

solution()
            
    
    
