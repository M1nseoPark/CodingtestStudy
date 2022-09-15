n, k = map(int, input().split())
answer = 0
coin = []

for _ in range(n):
    coin.append(int(input()))

for i in range(n-1, -1, -1):
    answer += (k // coin[i])
    k = k % coin[i]

print(answer)
