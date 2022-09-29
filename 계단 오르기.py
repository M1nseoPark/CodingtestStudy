# DP는 어려워ㅠㅠㅠ

n = int(input())
stair = [0] * 301   # stair = [] 하면 인덱스 에러
for i in range(n):
    stair[i] = int(input())

dp = [0] * 301

# 3번째 계단까지는 미리 초기화 시켜줘야 반복문을 돌릴 수 있음
dp[0] = stair[0]
dp[1] = stair[0] + stair[1]
dp[2] = max(stair[1] + stair[2], stair[0] + stair[2])

for i in range(3, n):
    # 한 번에 한 칸 넘는 경우와 두 칸 넘는 경우
    # 연속된 세 개의 계단을 밟으면 안됨
    dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i])


print(dp[n-1])
