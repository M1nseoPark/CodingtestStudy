n, m, k = map(int, input().split())

# a의 개수가 1~n개, z의 개수가 1~m개인 경우는 기본적으로 1번씩은 있음 
dp = [[1] * (m + 1) for _ in range(n+1)]  # dp[a의 개수][z의 개수]


# 왜 이런식이 되는지 정확히 이해는 안됨 
for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]


if dp[n][m] < k:
    print(-1)

else:
    result = ''
    while True:
        # a로만 이루어져 있거나 z로만 이루어진 경우 
        if n == 0 or m == 0:
            result += ('z' * m)
            result += ('a' * n)
            break

        # 맨 앞의 알파벳이 a일 때 가질 수 있는 단어의 개수는 dp[n-1][m]
        flag = dp[n-1][m]

        # k가 flag보다 작거나 같다면 맨 앞 알파벳이 a이고, 크다면 z임 
        if k <= flag:  
            result += 'a'
            n -= 1
        else:
            result += 'z'
            m -= 1
            k -= flag

    print(result)

    
        
