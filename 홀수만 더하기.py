t = int(input())
for i in range(1, t+1):
    arr = list(map(int, input().split()))
    answer = 0
    
    for j in range(10):
        if arr[j] % 2 == 1:
            answer += arr[j]

    print('#' + str(i) + ' ' + str(answer))
        
	
