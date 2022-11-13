'''
내가 생각한 방법
1 -> 1
2 -> 1+1, 2
3 -> 1+1+1, 1+2, 3
각각의 방법을 어떻게 구하지..?
'''

'''
정답
dp[1]은 arr[1]과 동일
dp[2]는 dp[1]+arr[1] 또는 arr[2] 중 큰 값
dp[3]은 dp[1]+arr[2], dp[2]+arr[1], dp[3] 중 큰 값
-> 2차원 dp에 약한 것 같다
'''

n = int(input())
arr = [0] + list(map(int, input().split()))

dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], arr[j] + dp[i-j])

print(dp[n])



    
