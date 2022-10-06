def pick(cnt):
    if cnt == 6:
        for i in series:
            print(i, end=' ')
        print()

    else:
        for i in range(1, arr[0]+1):
            if not visited[i] and (len(series) == 0 or series[-1] < arr[i]):
                series.append(arr[i])
                visited[i] = True
                pick(cnt+1)
                series.pop()
                visited[i] = False
            

while True:
    arr = list(map(int, input().split()))

    if arr[0] == 0:
        break

    series = []
    visited = [False for _ in range(arr[0]+1)]

    pick(0)
    print()
    
