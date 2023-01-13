tree = {}
tree[1] = [1, 1, 1]
tree[2] = [1, 2, 2]

tree = sorted(tree.items(), key=lambda x: x[1][2])
print(tree)
        
