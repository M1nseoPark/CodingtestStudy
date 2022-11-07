import math

n = int(input())
result = math.factorial(n)
answer = 0

for s in str(result)[::-1]:
    if s == '0':
        answer += 1
    else:
        break

print(answer)

