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
            series.append(arr[i])
            pick(cnt+1)
            series.pop()

pick(0)
