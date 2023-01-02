def solution(k, tangerine):
    kind = {}
    for t in tangerine:
        if t not in kind:
            kind[t] = 1
        else:
            kind[t] += 1
    
    kind = sorted(kind.items(), key=lambda x:x[1])
    
    count = 0
    answer = len(kind)
    for i in range(len(kind)):
        count += kind[i][1]
        answer -= 1
        
        if count == len(tangerine) - k:
            break
        elif count > len(tangerine) - k:
            answer += 1
            break
    
    return answer
