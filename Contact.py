import re

t = int(input())
for _ in range(t):
    a = input()
    p = re.compile('(100+1+|01)+')
    if p.fullmatch(a):
        print("YES")
    else:
        print("NO")
    
    

    

    
            
