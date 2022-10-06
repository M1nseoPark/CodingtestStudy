n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
series = []
visited = [False for _ in range(n)]

def pick(cnt):
    if cnt == m:
        for i in series:
            print(i, end=' ')
        print()

    else:
        for i in range(n):
            if not visited[i]:
                series.append(arr[i])
                visited[i] = True
                pick(cnt+1)
                series.pop()
                visited[i] = False

pick(0)
                
            
