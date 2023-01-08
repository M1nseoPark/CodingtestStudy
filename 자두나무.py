# 자두가 홀수번 움직이면 2번 나무에, 짝수번 움직이면 1번 나무에 있음

t, w = map(int, input().split())
tree = [0]
for _ in range(t):
    tree.append(int(input()))

dp = [[0] * (w + 1) for _ in range(t+1)]

for i in range(1, t+1):   # i-1 때문에 인덱스 1부터 시작해야 함
    if tree[i] == 1:
        dp[i][0] = dp[i-1][0] + 1
    else:
        dp[i][0] = dp[i-1][0]
        
    for j in range(1, w+1):   # j-1 때문에 인덱스 1부터 시작해야 함 
        if j % 2 == 0:   # 자두가 1번 나무에 있음
            if tree[i] == 1:   # 움직이지 않고 받아먹을 수 있음 
                dp[i][j] = dp[i-1][j] + 1
            else:   # 움직여서 받아먹거나, 그냥 그대로 있거나 
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + 1)

        else:   # 자두가 2번 나무에 있음
            if tree[i] == 2:   # 움직이지 않고 받아먹을 수 있음 
                dp[i][j] = dp[i-1][j] + 1
            else:   # 움직여서 받아먹거나, 그냥 그대로 있거나 
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + 1)


print(max(dp[-1]))  
