n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

A.sort()

def binarySearch(target):
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2
        if A[mid] == target:
            print(1)
            break

        elif A[mid] > target:
            right = mid - 1

        else:
            left = mid + 1

    if left > right:
        print(0)


for i in range(m):
    binarySearch(B[i])
        
    
