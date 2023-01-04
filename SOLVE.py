n = int(input())
tree = {}
for _ in range(n):
    a, b, c = input().split()
    tree[a] = [b, c]

pre = ''
ino = ''
pos = ''

def preorder(v):
    global pre
    
    if v != '.':
        pre += v
        preorder(tree[v][0])
        preorder(tree[v][1])


def inorder(v):
    global ino
    
    if v != '.':
        inorder(tree[v][0])
        ino += v
        inorder(tree[v][1])


def postorder(v):
    global pos
    
    if v != '.':
        postorder(tree[v][0])
        postorder(tree[v][1])
        pos += v
        

preorder('A')
inorder('A')
postorder('A')

print(pre)
print(ino)
print(pos)
