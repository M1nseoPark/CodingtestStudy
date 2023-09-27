def find_parent(parent, x):
    if parent[x] != x:
        find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

test = int(input())
for _ in range(test):
    f = int(input())
    parent = {}

    a, b = input().split()
    if a not in parent:
        parent[a] = [a]
    if b not in parent:
        parent[b] = [b]

    union_parent(parent, a, b)