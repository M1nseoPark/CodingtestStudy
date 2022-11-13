import sys

m, n = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

left = 1
right = max(arr)

while left <= right:
    mid = (left + right) // 2

    temp = 0
    for i in range(n):
        temp += (arr[i] // mid)

    if temp >= m:
        left = mid + 1
    else:
        right = mid -1

print(right)
        
