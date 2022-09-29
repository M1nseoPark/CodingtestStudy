n, m = map(int, input().split())
tree = list(map(int, input().split()))

tree.sort()

def binarySearch(target):
    answer = 0
    left = 0
    right = n - 1
    
    if answer >= m:
        print(target)
        break

    mid = (left + right) // 2

    if tree[mid] > target:
        
    

    
    
