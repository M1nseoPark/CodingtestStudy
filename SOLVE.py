import sys

n, m = map(int, sys.stdin.readline().split())
memory = [0] + list(map(int, sys.stdin.readline().split()))
cost = [0] + list(map(int, sys.stdin.readline().split()))

# dp[i][j] = i번째 앱까지 살펴봤을 때, j만큼의 비용 사용하여 확보할 수 있는 최대 메모리 
dp = [[0] * 10001 for _ in range(n+1)] 
answer = float('inf')

for i in range(1, n+1):
    for j in range(1, 10001):
        M = memory[i]
        c = cost[i]

        if j < c:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-c] + M)

        if dp[i][j] >= m:
            answer = min(j, answer)
            break
            

print(answer)
        
        
        



    
