import math

n, k = map(int, input().split())
answer = math.factorial(n) // (math.factorial(k) * math.factorial(n-k))

print(answer % 10007)
