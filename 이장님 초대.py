n = int(input())
tree = list(map(int, input().split()))

tree.sort(reverse=True)
for i in range(n):
    tree[i] = tree[i] + (i + 1)

print(max(tree) + 1)
    
