n, m = map(int, input().split())

series = []
visited = [False for _ in range(n+1)]

def pick(cnt):
    if cnt == m:
        for i in series:
            print(i, end=' ')
        print()

    else:
        for i in range(1, n+1):
            if not visited[i] and (len(series) == 0 or series[-1] < i):
                series.append(i)
                visited[i] = True
                pick(cnt+1)
                series.pop()
                visited[i] = False

pick(0)
