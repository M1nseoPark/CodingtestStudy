# 메모리 초과
# 음수일때는 나머지 연산을 어떻게 해야하는지
## 음수일 때 피보나치 수열 = 0, 1, -1, 2, -3, 5, ...

n = int(input())

if n == 0:
    print(0)
    print(0)
else:
    dp = [0 for _ in range(abs(n)+1)]
    dp[1] = 1

    for i in range(2, abs(n)+1):
        dp[i] = (dp[i-1] % 1000000000) + (dp[i-2] % 1000000000)

    if n < 0 and abs(n) % 2 == 0:
        print(-1)
    else:
        print(1)

    print(dp[abs(n)])
    
        
    
    
