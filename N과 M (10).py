n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
visited = [False for _ in range(n)]
series = []

def pick(cnt):
    temp = 0
    
    if cnt == m:
        for i in series:
            print(i, end=' ')
        print()

    else:
        for i in range(n):
            if not visited[i] and temp != arr[i]:
                if len(series) == 0 or series[-1] <= arr[i]:
                    series.append(arr[i])
                    visited[i] = True
                    temp = arr[i]

                    pick(cnt+1)
                    series.pop()
                    visited[i] = False

pick(0)
