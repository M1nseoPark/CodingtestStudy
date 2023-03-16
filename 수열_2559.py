n, k = map(int, input().split())
arr = list(map(int, input().split()))

t = sum(arr[:k])
answer = t

for i in range(1, n-k+1):
    t -= arr[i-1]
    t += arr[i+k-1]
    if t > answer:
        answer = t

print(answer)
    
