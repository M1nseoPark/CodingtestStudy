n = int(input())
score = []
for _ in range(n):
    score.append(list(map(int, input().split())))

def dfs(d, idx):
    global answer
    if d == n//2:
        ans1, ans2 = 0, 0
        for i in range(n):
            for j in range(n):
                if pick[i] and pick[j]:
                    ans1 += score[i][j]
                elif not pick[i] and not pick[j]:
                    ans2 += score[i][j]

        answer = min(answer, abs(ans1 - ans2))
        return

    else:
        for i in range(idx, n):
            if not pick[i]:
                pick[i] = True
                dfs(d+1, i+1)
                pick[i] = False
        
pick = [False] * n
answer = float('inf')
dfs(0, 0)
print(answer)
