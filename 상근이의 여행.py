from collections import deque

test = int(input())

for _ in range(test):
    n, m = map(int, input().split())
    air = [[0] * (n + 1) for i in range(n+1)]
    for i in range(m):
        a, b = map(int, input().split())

    print(n-1)

    
