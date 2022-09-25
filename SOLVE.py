n = int(input())
seat = input()

s = 1
i = 0

while i < n:
    if seat[i] == 'S':
        s += 1

    if seat[i] == 'L':
        s += 1
        i += 1

    i+= 1

print(min(s, n))
        
    
    
    
    
        
    
    

    

            



        




    
