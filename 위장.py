def solution(clothes):
    count = {}
    for i in range(len(clothes)):
        if clothes[i][1] not in count:
            count[clothes[i][1]] = [clothes[i][0]]
        else:
            count[clothes[i][1]].append(clothes[i][0])
    
    answer = 1
    for i in count:
        answer *= len(count[i]) + 1
    
    answer -= 1
        
    return answer
