t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    answer = 0
    maxi = 0
    for i in range(n-1, -1, -1):
        if maxi <= arr[i]:
            maxi = arr[i]
        else:
            answer += (maxi - arr[i])

    print(answer)
        
        
