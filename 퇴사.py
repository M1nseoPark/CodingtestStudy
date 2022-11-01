n = int(input())
consult = []
for _ in range(n):
    consult.append(list(map(int, input().split())))

dp = [0 for _ in range(n+1)]

for i in range(n-1, -1, -1):
    if consult[i][0] + i <= n:   # 날짜를 초과하지 않을 경우
        # max(상담 금액 + dp[상담 끝마친 시간], 해당 상담을 하지 않았을 때)
        dp[i] = max(consult[i][1] + dp[i + consult[i][0]], dp[i+1])
    else:   # 날짜를 초과할 경우
        dp[i] = dp[i+1]

print(dp[0])
