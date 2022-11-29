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

n, m = map(int, input().split())
arr = []
for _ in range(n):
    temp = list(map(int, input().split()))
    arr.append([[temp[i], i] for i in range(m)])

def equal(arr1, arr2):
    arr1.sort()
    arr2.sort()
    for i in range(m):
        if arr1[i][1] != arr2[i][1]:
            return False

    return True


answer = 0
for i in range(n):
    for j in range(i+1, n):
        if equal(arr[i], arr[j]):
            answer += 1

print(answer)

        
        
        

