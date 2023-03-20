n, m, h = map(int, input().split())
line = [[0] * (n + 1) for _ in range(h+1)]
for _ in range(m):
    a, b = map(int, input().split())
    line[a][b] = 1

sub = []   # 사다리 놓을 수 있는 위치 후보 
for i in range(1, h+1):
    for j in range(1, n):
        if line[i][j] == 0 and line[i][j-1] == 0 and line[i][j+1] == 0:
            sub.append([i, j])


def check():
    for i in range(1, n+1):
        now = i   # 현재 몇번 세로선에 있는지 
        for j in range(1, h+1):   # 사다리 맨위에서 맨아래까지 
            if line[j][now] == 1:
                now += 1
            elif line[j][now-1] == 1:
                now -= 1

        if i != now:   # i번 세로선의 결과가 i번이 아니면 
            return False
    return True
    

def dfs(cnt, num):   # 놓아야 하는 사다리 수, 몇번째 후보까지 검사했는지 
    global answer
    if cnt >= answer:   # 사다리를 예전에 구한 정답보다 많이 놓아야 하면
        return

    if check():
        answer = cnt
        return

    for idx in range(num+1, len(sub)):
        i, j = sub[idx]
        if line[i][j-1] == 0 and line[i][j+1] == 0:
            line[i][j] = 1
            dfs(cnt+1, idx)
            line[i][j] = 0

            
answer = 4
dfs(0, -1)
if answer < 4:
    print(answer)
else:
    print(-1)
    

