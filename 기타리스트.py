n, s, m = map(int, input().split())
V = list(map(int, input().split()))

def dfs(idx, rst):
    global answer
    
    if rst < 0 or rst > m:
        return

    if idx == n:
        answer = max(rst, answer)
        return

    dfs(idx+1, rst+V[idx])
    dfs(idx+1, rst-V[idx])
    

answer = 0
dfs(0, s)

if answer == 0:
    print(-1)
else:
    print(answer)

    
