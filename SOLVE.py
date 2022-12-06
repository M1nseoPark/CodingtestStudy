n = int(input())
arr = list(map(int, input().split()))

arr.sort()
result = 3000000000
answer = [0, 0, 0]

for i in range(n-2):
    a = arr[i]

    left = i + 1
    right = n - 1
    while left < right:
        temp = a + arr[left] + arr[right]

        if abs(temp) < result:
            result = abs(temp)
            answer[0], answer[1], answer[2] = arr[i], arr[left], arr[right]

        if temp == 0:
            break

        elif temp < 0:
            left += 1

        else:
            right -= 1


print(answer[0], answer[1], answer[2])
            

    

    


    
    




        
        
        

