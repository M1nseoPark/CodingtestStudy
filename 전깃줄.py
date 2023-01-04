n = int(input())
wire = []
for _ in range(n):
    wire.append(list(map(int, input().split())))

wire.sort()
arr = []
for i in range(n):
    arr.append(wire[i][1])

dp = [1] * (n + 1)
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))
