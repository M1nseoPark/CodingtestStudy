n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
series = []
result = []
visited = [False for _ in range(n)]

def pick(cnt):
    temp = 0  # 중복 수열인지 확인하기 위해 필요한 임시 변수
    
    if cnt == m:
        for i in series:
            print(i, end=' ')
        print()

    else:
        for i in range(n):
            # 이전 수열의 마지막 항과 새로운 수열의 마지막 항이 같으면 중복 수열???
            if not visited[i] and temp != arr[i]:
                series.append(arr[i])
                visited[i] = True
                temp = series[-1]
                
                pick(cnt+1)
                series.pop()
                visited[i] = False

pick(0)
