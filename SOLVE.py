n = int(input())
row = [0 for _ in range(n)]

def adjacent(d):
    for i in range(d):
        if row[i] == row[d]:
            return False

        if d - i == abs(row[i] - row[d]):
            return False

    return True


answer = 0
for i in range(n):
    for j in range(n):
        row[i] = j
        if adjacent(i):
            answer += 1
            break

print(answer)
    
    
    




        
    
        
    
                    
    

    



    
