n, m = map(int, input().split())

series = []

def pick(cnt):
    if cnt == m:
        for i in series:
            print(i, end=' ')
        print()

    else:
        for i in range(1, n+1):
            if len(series) == 0 or series[-1] <= i:
                series.append(i)
                pick(cnt+1)
                series.pop()

pick(0)
