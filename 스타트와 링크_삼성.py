n = int(input())
s = []
for _ in range(n):
    s.append(list(map(int, input().split())))

start = []
link = []
visited = [False for _ in range(n)]
answer = 100

def pick(cnt):
    global answer

    if cnt == n // 2:
        # 링크 팀 구하기
        for i in range(n):
            if not visited[i]:
                link.append(i)

        # 능력치 차이 계산하기
        sscore, lscore = 0, 0
        for i in range(n//2):
            for j in range(n//2):
                sscore += s[start[i]][start[j]]
                lscore += s[link[i]][link[j]]

        answer = min(answer, abs(sscore - lscore))
        link.clear()

    else:
        # 스티트 팀 구하기
        for i in range(n):
            if not visited[i] and (len(start) == 0 or start[-1] < i):
                start.append(i)
                visited[i] = True
                pick(cnt+1)
                start.pop()
                visited[i] = False

pick(0)
print(answer)
