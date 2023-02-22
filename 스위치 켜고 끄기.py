n = int(input())
arr = [0] + list(map(int, input().split()))
s = int(input())
for _ in range(s):
    a, b = map(int, input().split())
    if a == 1:
        for i in range(b, n+1, b):
            if arr[i] == 0:
                arr[i] = 1
            else:
                arr[i] = 0
    else:
        if arr[b] == 0:
            arr[b] = 1
        else:
            arr[b] = 0
                    
        for i in range(1, min(b, n-b+1)):
            if arr[b-i] == arr[b+i]:
                if arr[b-i] == 0:
                    arr[b-i], arr[b+i] = 1, 1
                else:
                    arr[b-i], arr[b+i] = 0, 0
            else:
                break

for i in range(1, n+1, 20):
    print(' '.join(map(str, arr[i:i+20])))
                
            
            
        

