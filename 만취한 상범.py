t = int(input())

for _ in range(t):
    n = int(input())

    arr = [True for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(i, n+1, i):
            if arr[j]:
                arr[j] = False
            else:
                arr[j] = True

    answer = 0
    for i in range(1, n+1):
        if not arr[i]:
            answer += 1

    print(answer)
                
