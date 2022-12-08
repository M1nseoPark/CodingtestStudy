n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))

dp = [0 for _ in range(k+1)]  # 합이 i원이 되는 경우의 수
dp[0] = 1

for i in coin:   # 각 코인의 종류 순회(1원, 2원, 5원)
    for j in range(i, k+1):  # i원부터 순회
        if j - i >= 0:
            # dp[3] = dp[3] + dp[1] -> 1원짜리 동전 이용(1+1+1) + 1원과 2원 동전 이용(1+2)
            dp[j] += dp[j-i]

print(dp[k])

