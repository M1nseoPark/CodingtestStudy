import sys

n = int(sys.stdin.readline())
egg = []
for _ in range(n):
    egg.append(list(map(int, sys.stdin.readline().split())))

answer = 0

def hit(idx):
    global answer
    
    if idx == n:
        temp = 0
        for i in range(n):
            if egg[i][0] <= 0:
                temp += 1

        answer = max(temp, answer)
        return


    if egg[idx][0] > 0:
        remain = False
        for i in range(n):
            if idx != i and egg[i][0] > 0:
                remain = True
                break
        
        if remain:        
            for i in range(n):
                if idx != i and egg[i][0] > 0:
                    egg[idx][0] -= egg[i][1]
                    egg[i][0] -= egg[idx][1]
                    hit(idx + 1)
                    egg[idx][0] += egg[i][1]
                    egg[i][0] += egg[idx][1]
        else:
            hit(idx + 1)
    else:
        hit(idx + 1)


hit(0)
print(answer)
            
            
            


            

    
            
            


                

            
    
    




    
    
