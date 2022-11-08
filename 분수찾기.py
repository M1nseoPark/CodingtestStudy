x = int(input())

idx, i, d = 0, 0, 0
while idx < x:
    i += 1
    idx += i
    d += 1

# 굳이 반복문을 쓸 필요 없이 idx-x를 더하고 빼면 되는 거였음..
if d % 2 == 1:
    a, b = i, 1
    for j in range(idx-x):
        a -= 1
        b += 1
    print(str(b) + '/' + str(a))
    
else:
    a, b = i, 1
    for j in range(idx-x):
        a -= 1
        b += 1
    print(str(a) + '/' + str(b))
        
        
        
        
        



    
    
