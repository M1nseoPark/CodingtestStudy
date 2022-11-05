# 부분문제의 최대값이 전체의 최대값이 아님.. -> 움직인 횟수를 추가로 고려해줘야 하는데 모르겠다
## X초에 Y번 움직여서 먹은 자두의 최대 개수 -> 변수가 2개이므로 2차원 dp
## 자두가 홀수번 움직이면 2번 나무에, 짝수번 움직이면 1번 나무에 있음

t, w = map(int, input().split())  # 자두는 t초 동안 떨어짐, 자두는 최대 w번만 움직일 수 있음
tree = [0 for _ in range(t+1)]
for i in range(1, t+1):
    tree[i] = int(input())

dp = [[0] * (w + 1) for _ in range(t+1)]  

for i in range(1, t+1):
    # 한 번도 움직이지 않았을 때, 1번에서 떨어질 때만 받아 먹을 수 있음
    if tree[i] == 1:
        dp[i][0] = dp[i-1][0] + 1
    else:
        dp[i][0] = dp[i-1][0]

    # 이동 횟수를 1번부터 w번까지 움직이면서 체크
    for j in range(1, w+1):
        if tree[i] == 1 and j % 2 == 0:  # 이동 횟수가 짝수번이면 1번 나무에
            # 움직여서 받아먹거나, 현재 위치에서 받아먹거나
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1

        elif tree[i] == 2 and j % 2 == 1:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1

        else:
            # 그대로 있거나 움직여서 안먹음
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])


print(max(dp[-1]))
