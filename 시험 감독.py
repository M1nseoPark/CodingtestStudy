import math

n = int(input())
A = list(map(int, input().split()))
b, c = map(int, input().split())

answer = n

for i in range(n):
    if A[i] - b > 0:
        answer += math.ceil((A[i] - b) / c)

print(answer)
