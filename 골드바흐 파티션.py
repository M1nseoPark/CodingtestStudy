import sys

t = int(sys.stdin.readline())

arr = [True for _ in range(1000001)]

def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if arr[i]:
            for j in range(i+i, n+1, i):
                arr[j] = False
                
                
for _ in range(t):
    n = int(sys.stdin.readline())

    isPrime(n)

    s = n // 2
    answer = 0
    
    while s != 1:
        if arr[s] and arr[n-s]:
            answer += 1
        s -= 1

    print(answer)
