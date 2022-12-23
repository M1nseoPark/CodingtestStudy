n = int(input())
tree = []

def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')


tree = {}
for _ in range(n):
    temp = list(input().split())
    tree[temp[0]] = [temp[1], temp[2]]


preorder('A')
print()
inorder('A')
print()
postorder('A')
