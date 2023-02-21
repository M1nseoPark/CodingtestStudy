k = int(input())
arr = list(map(int, input().split()))
tree = [[] for _ in range(k)]

def inorder(first, last, k):
    if first == last:
        tree[k].append(arr[first])
        return

    mid = (first + last) // 2
    tree[k].append(arr[mid])
    inorder(first, mid-1, k+1)
    inorder(mid+1, last, k+1)


inorder(0, len(arr)-1, 0)
for i in range(k):
    for j in tree[i]:
        print(j, end=' ')
    print()
    
