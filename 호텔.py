c, n = map(int, input().split())
city = []
for _ in range(n):
    city.append(list(map(int, input().split())))

dp = [100000] * (c + 100)
dp[0] = 0

for i in range(n):
    for j in range(city[i][1], c+100):
        dp[j] = min(dp[j-city[i][1]] + city[i][0], dp[j])

print(min(dp[c:]))

