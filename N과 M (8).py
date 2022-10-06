n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
series = []

def pick(cnt):
    if cnt == m:
        for i in series:
            print(i, end=' ')
        print()

    else:
        for i in range(n):
            if len(series) == 0 or series[-1] <= arr[i]:
                series.append(arr[i])
                pick(cnt+1)
                series.pop()

pick(0)
