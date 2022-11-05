n = int(input())
arr = list(map(int, input().split()))

answer = 0
for i in range(n):
    if arr[i] == 1:
        continue

    else:
        prime = True
        for j in range(2, arr[i]):
            if arr[i] % j == 0:
                prime = False
                break

        if prime:
            answer += 1


print(answer)
            
            
