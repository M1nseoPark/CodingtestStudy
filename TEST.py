n, m, h = map(int, input().split())
line = [[0] * n for _ in range(h)]
for i in range(m):
    a, b = map(int, input().split())
    line[a-1][b-1] = 1

sub = []
answer = 400
for i in range(h):
    for j in range(n-1):
        if line[i][j] == 0:
            if j == 0:
                if line[i][j+1] == 0:
                    sub.append([i, j])
            elif j == n - 1:
                if line[i][j-1] == 0:
                    sub.append([i, j])
            else:
                if line[i][j-1] == 0 and line[i][j+1] == 0:
                    sub.append([i, j])


def check():
    for i in range(n):
        now = i
        for j in range(h):
            if now == 0 and line[j][now] == 1:
                now += 1
            elif now == (n - 1) and line[j][now-1] == 1:
                now -= 1
            elif 0 < now < (n - 1):
                if line[j][now-1] == 1:
                    now -= 1
                elif line[j][now] == 1:
                    now += 1
            print(now)
        print('----')
        if now != i:
            return False
    
    return True


def dfs(cnt):
    global answer
    if cnt > 3:
        return

    if check():
        answer = min(answer, cnt)
        return
    
    for i in range(len(sub)):
        line[sub[i][0]][sub[i][1]] = 1
        dfs(cnt + 1)
        line[sub[i][0]][sub[i][1]] = 0


dfs(0)

if answer == 400:
    print(-1)
else:
    print(answer)
