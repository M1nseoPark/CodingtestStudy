import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

for i in range(1, n):
    arr[i] += arr[i-1]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if a == 1:
        print(arr[b-1])
    else:
        print(arr[b-1] - arr[a-2])
