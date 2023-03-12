k = int(input())
A = list(map(int, input().split()))

tree = [[] for _ in range(k)]

def find(depth, s, e):
    if depth == k:
      return
  
    mid = (s + e) // 2
    find(depth+1, s, mid)
    find(depth+1, mid+1, e)
    tree[depth].append(A[mid])

find(0, 0, len(A))
for i in range(k):
    print(' '.join(map(str, tree[i])))


