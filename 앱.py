n, m = map(int, input().split())   # n 이상의 메모리 확보 필요 
A = [0] + list(map(int, input().split()))   # 각 앱이 사용 중인 메모리 
cost = [0] + list(map(int, input().split()))   # 비활성화 했을 때 비용(최소화해야 함)

k = sum(cost)
# dp[i][j] = i번째 앱까지 살펴봤을 때, j만큼의 비용 사용하여 확보할 수 있는 최대 메모리 
dp = [[0] * (k + 1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        w = A[i]
        v = cost[i]

        if j < v:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(w + dp[i-1][j-v], dp[i-1][j])

        if dp[i][j] >= m:
            result = min(result, j)

if m != 0:
    print(result)
else:
    print(0)
