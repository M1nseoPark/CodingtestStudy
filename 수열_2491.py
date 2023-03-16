n = int(input())
A = list(map(int, input().split()))

dp1 = [1] * n
for i in range(1, n):
    if A[i-1] <= A[i]:
        dp1[i] = dp1[i-1] + 1
    else:
        dp1[i] = 1

dp2 = [1] * n
for i in range(1, n):
    if A[i-1] >= A[i]:
        dp2[i] = dp2[i-1] + 1
    else:
        dp2[i] = 1

print(max(max(dp1), max(dp2)))
