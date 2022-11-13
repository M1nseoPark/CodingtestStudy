import sys

n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

left = 0
right = max(tree)

while left <= right:
    mid = (left + right) // 2

    temp = 0
    for i in range(n):
        if tree[i] - mid >= 0:
            temp += (tree[i] - mid)
        if temp > m:   # 절단된 나무를 추가하는 중에 이미 m을 넘으면 중단
            break

    if temp >= m:
        left = mid + 1
    else:
        right = mid - 1

print(right)
                

            
    
    




    
    
