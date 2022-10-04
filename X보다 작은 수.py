n, x = map(int, input().split())
A = list(map(int, input().split()))

for i in range(n):
    if x > A[i]:
        print(A[i], end=' ')
