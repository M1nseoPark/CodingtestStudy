n, m = map(int, input().split())
series = []
visited = [False for _ in range(n+1)]

def pick(cnt):
    if cnt == m:
        for i in series:
            print(i, end=' ')
        print()

    else:
        # k = m이 아니라면 1과 n까지의 수를 차례로 확인하여 아직 쓰이지 않은 수를 찾아냄
        for i in range(1, n+1):
            if not visited[i]:
                series.append(i)
                visited[i] = True
                pick(cnt+1)
                series.pop()
                visited[i] = False


pick(0)
