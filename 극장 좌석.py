# 처음에 짰던 코드도 알고리즘은 다 맞았는데 왜 틀렸는지 모르겠음..
# 최대한 반복문을 줄이고 코드를 간단히 짜자!

n = int(input())
m = int(input())

dp = [0 for _ in range(n+1)]
dp[0] = 1
dp[1] = 1
for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]


if m == 0:
    print(dp[n])
    
else:
    tmp = 0
    answer = 1
    
    for i in range(m):
        vip = int(input())
        answer *= dp[vip-tmp-1]
        tmp = vip
        
    answer *= dp[n-tmp]

    print(answer)
        
