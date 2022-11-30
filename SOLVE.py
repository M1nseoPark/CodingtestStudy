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

# m!/(n-m)!
n, m = map(int, input().split())

def count(num, d):
    rst = 0
    while True:
        if num % d == 0:
            num //= d
            rst += 1
        else:
            break

    return rst
        

two = count(m, 2) - count(n-m, 2)
five = count(m, 2) - count(n-m, 5)

print(min(two, five))

    
    




        
        
        

