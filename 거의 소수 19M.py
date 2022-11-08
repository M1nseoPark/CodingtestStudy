a, b = map(int, input().split())

arr = [True for _ in range(b+1)]
rst = [False for _ in range(b+1)]
arr[1] = False

def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if arr[i]:
            for j in range(i+i, n+1, i):
                arr[j] = False

isPrime(b)
for i in range(2, b+1):
    if arr[i]:
        d = 2
        while i**d <= b:
            rst[i**d] = True
            d += 1

answer = 0
for i in range(a, b+1):
    if rst[i]:
        answer += 1

print(answer)
            
