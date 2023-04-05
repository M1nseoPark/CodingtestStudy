from itertools import combinations

def solution(relation):
    answer = 0
    n = len(relation)
    m = len(relation[0])
    
    combi = []
    for i in range(1, n+1):
        combi.extend(combinations(range(m), i))
    
    key = []
    for c in combi:
        result = set()
        
        for i in range(n):
            temp = []
            for j in c:
                temp.append(relation[i][j])
            result.add(tuple(temp))
        
        if len(result) == n:
            flag = True
            for i in range(len(key)):
                if key[i].issubset(set(c)):
                    flag = False
                    break
            
            if flag:
                key.append(set(c))
                answer += 1
                    
    return answer
