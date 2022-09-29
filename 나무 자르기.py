import sys

n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
left, right = 1, max(tree)   # left, right값을 인덱스로 할 필요는 없음

while left <= right:
    mid = (left + right) // 2

    result = 0
    for i in range(n):
        if tree[i] >= mid:
            result += tree[i] - mid

    if result >= m:
        left = mid + 1
    else:
        right = mid - 1

print(right)
    

    

    
    
        
    

    
    
