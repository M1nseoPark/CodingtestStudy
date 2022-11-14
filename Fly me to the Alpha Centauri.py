t = int(input())

for _ in range(t):
    x, y = map(int, input().split())

    dp = []
    idx, k = 1, 1
    while len(dp) <= y - x:
        dp += [idx] * k
        idx += 1
        if idx != 1 and idx % 2 == 1:
            k += 1

    print(dp[y-x-1])
        
    
