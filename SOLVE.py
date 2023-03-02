import copy

n = int(input())
dp1 = list(map(int, input().split()))
dp2 = copy.deepcopy(dp1)

for _ in range(1, n):
    game = list(map(int, input().split()))
    for i in range(3):
        if i == 0:
            dp1[i] += max(game[i], game[i+1])
            dp2[i] += min(game[i], game[i+1])
            
        elif i == 2:
            dp1[i] += max(game[i-1], game[i])
            dp2[i] += min(game[i-1], game[i])
            
        else:
            dp1[i] += max(game[i-1], game[i], game[i+1])
            dp2[i] += min(game[i-1], game[i], game[i+1])

print(max(dp1), min(dp2))
