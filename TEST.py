data = input()

stack = []
ans = 0
for i in range(len(data)):
    if data[i] == '(':
        stack.append('(')
    else:
        if data[i-1] == '(':
            stack.pop()
            ans += len(stack)
        else:
            ans += 1
            stack.pop()
            
print(ans)
        
    
    
