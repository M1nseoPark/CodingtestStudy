from collections import Counter

def solution(a):
    answer = -1
    dic = Counter(a)

    for k, v in dic.items():
        if v <= answer:
            continue

        cnt, idx = 0, 0  
        while idx < len(a) - 1:
            if (a[idx] != k and a[idx+1] != k) or (a[idx] == a[idx+1]):
                idx += 1
                continue
            
            cnt += 1
            idx += 2
        
        answer = max(cnt, answer)
    
    if answer == -1:
        return -1
    
    return answer * 2
        
