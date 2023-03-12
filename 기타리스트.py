n, s, m = map(int, input().split())
V = [0] + list(map(int, input().split()))

dp = [[0] * (m + 1) for _ in range(n+1)]
dp[0][s] = 1

for i in range(1, n+1):
    for j in range(m+1):
        if dp[i-1][j] == 1:
            if j + V[i] <= m:
                dp[i][j+V[i]] = 1
            if j - V[i] >= 0:
                dp[i][j-V[i]] = 1

answer = -1
for i in range(m, -1, -1):
    if dp[n][i] == 1:
        answer = i
        break

print(answer)
