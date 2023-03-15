n = int(input())
color = []
for _ in range(n):
    color.append(list(map(int, input().split())))

answer = float('inf')
for i in range(3):
    dp = [[-1] * 3 for _ in range(n+1)]
    dp[0] = [float('inf'), float('inf'), float('inf')]
    dp[0][i] = color[0][i]

    for i in range(1, n):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + color[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + color[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + color[i][2]

    dp[n-1][i] = float('inf')
    answer = min(answer, min(dp[n-1]))

print(answer)


