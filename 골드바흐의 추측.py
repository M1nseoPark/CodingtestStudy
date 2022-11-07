t = int(input())

arr = [True for _ in range(10001)]

def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if arr[i]:
            for j in range(i+i, n+1, i):
                arr[j] = False

    
for _ in range(t):
    n = int(input())

    isPrime(n)

    s = n // 2
    
    while True:
        if arr[s]:
            if arr[n-s]:
                break
            else:
                s -= 1
        else:
            s -= 1

    print(s, n - s)
        
