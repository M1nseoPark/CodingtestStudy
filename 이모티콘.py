s = int(input())
dp = [[-1] * (s + 1) for _ in range(s+1)]
q = []
q.append([1, 0])   # 화면 이모티콘 개수, 클립보드 이모티콘 개수
dp[1][0] = 0

while q:
    n, c = q.pop(0)
    if dp[n][n] == -1:   
        dp[n][n] = dp[n][c] + 1   # 클립보드에 저장
        q.append([n, n])

    if n + c <= s and dp[n+c][c] == -1:
        dp[n+c][c] = dp[n][c] + 1   # 화면에 붙여넣기(클립보드는 그대로)
        q.append([n+c, c])

    if n - 1 >= 0 and dp[n-1][c] == -1:
        dp[n-1][c] = dp[n][c] + 1   # 화면에 있는 이모티콘 하나 삭제(클립보드는 그대로)
        q.append([n-1, c])


answer = -1
for i in range(s+1):   # 클립보드 개수와 상관없이 화면 이모티콘 개수가 s인 것 중에서
    if dp[s][i] != -1:
        if answer == -1 or answer > dp[s][i]:   # 걸리는 시간의 최솟값 구함
            answer = dp[s][i]

print(answer)
    
