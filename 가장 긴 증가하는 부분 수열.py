import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

dp = [1 for _ in range(n)]

for i in range(1, n):
    if A[s] < A[i]:
        ret = max(ret, lis(i) + 1)
     
print(lis(0))
