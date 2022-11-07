import math

arr = [True for _ in range(300000)]
arr[0] = False
arr[1] = False

def prime(n):
    answer = 0

    for i in range(2, int(math.sqrt(2*n))+1):
        if arr[i]:
            for j in range(i+i, 2*n+1, i):
                arr[j] = False

    for i in range(n+1, 2*n+1):
        if arr[i]:
            answer += 1

    return answer
    

while True:
    n = int(input())

    if n == 0:
        break

    print(prime(n))

    
