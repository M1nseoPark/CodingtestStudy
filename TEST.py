for _ in range(3):
    n = int(input())
    coin = []
    total = 0
    for i in range(n):
        a, b = map(int, input().split())
        coin.append([a, b])
        total += a * b

    if total % 2 == 1:
        print(0)
        continue

    total //= 2
    dp = [True] + [False] * (total + 1)
    answer = 0

    for i in range(n):
        k, c = coin[i]

        for j in range(total, k-1, -1):
            if dp[j-k]:
                for t in range(c):
                    if j + k * t <= total:
                        
        

    

        
