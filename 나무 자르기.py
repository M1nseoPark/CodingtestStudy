n, m = map(int, input().split())
tree = list(map(int, input().split()))

tree.sort(reverse=True)

cut = 1
answer = tree[n-1] - 1
for i in range(1, n):
    if tree[i] <= answer:
        if cut >= m:
            print(answer)
        else:
            answer -= 1
            tree += (i + 1)

    

    
    
        
    

    
    
