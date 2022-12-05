'''
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()
left, right = 0, n-1
answer = 3000000000

while left <= right:
    temp = abs(arr[right] - arr[left])

    if temp >= m:
        answer = min(answer, temp)
        left += 1

    else:
        right -= 1

print(answer)
'''



    


    
    




        
        
        

