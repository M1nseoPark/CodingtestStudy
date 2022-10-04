n = int(input())
answer = 0
for i in range(1, n):
    if 2 ** i > n:
        answer = i - 1
        break

print(2 ** answer)
