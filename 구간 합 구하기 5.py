import sys

n, m = map(int, sys.stdin.readline().split())
table = []
for _ in range(n):
    table.append(list(map(int, sys.stdin.readline().split())))

dp = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == 0:
            if j == 0:
                dp[i][j] = table[i][j]
            else:
                dp[i][j] = dp[i][j-1] + table[i][j]
        
        elif j == 0:
            dp[i][j] = dp[i-1][j] + table[i][j]
            
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1] + table[i][j] - dp[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    x2 -= 1; x1 -= 1; y2 -= 1; y1 -= 1

    if x1 == 0 and y1 == 0:
        print(dp[x2][y2])
    elif y1 == 0:
        print(dp[x2][y2] - dp[x1-1][y2])
    elif x1 == 0:
        print(dp[x2][y2] - dp[x2][y1-1])
    else:
        print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])

