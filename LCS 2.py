str1 = input()
str2 = input()

dp = [[''] * (len(str2) + 1) for _ in range(len(str1)+1)]
for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + str1[i-1]
        else:
            if len(dp[i-1][j]) >= len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

if len(dp[len(str1)][len(str2)]) == 0:
    print(0)
else:
    print(len(dp[len(str1)][len(str2)]))
    print(dp[len(str1)][len(str2)])
