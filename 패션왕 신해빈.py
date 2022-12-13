test = int(input())
for _ in range(test):
    n = int(input())
    clothes = {}
    for i in range(n):
        a, b = input().split()
        if len(clothes) == 0 or b not in clothes:
            clothes[b] = [a]
        else:
            clothes[b].append(a)

    answer = 1
    
    for i in clothes:
        answer *= (len(clothes[i])+1)
            
    print(answer-1)
    
        
