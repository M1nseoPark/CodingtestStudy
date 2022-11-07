n, k = map(int, input().split())

arr = [True for _ in range(n+1)]
idx = 0

for i in range(2, n+1):
    for j in range(i, n+1, i):
        if arr[j]:
            arr[j] = False
            idx += 1

            if idx == k:
                print(j)
                break
        
    
