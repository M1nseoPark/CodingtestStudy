def solution(picks, minerals):
    m = sum(picks) * 5
    n = len(minerals)
    if n > m:
        minerals = minerals[:m]
    
    arr = [[0, 0, 0] for _ in range(10)]
    for i in range(len(minerals)):
        if minerals[i] == 'diamond':
            arr[i//5][0] += 1
        elif minerals[i] == 'iron':
            arr[i//5][1] += 1
        else:
            arr[i//5][2] += 1
    
    arr.sort(reverse=True)
    
    answer = 0
    for k in range(len(arr)):
        d, i, s = arr[k]
        
        if picks[0] > 0:
            answer += d + i + s
            picks[0] -= 1
        elif picks[1] > 0:
            answer += d * 5 + i + s
            picks[1] -= 1
        elif picks[2] > 0:
            answer += d * 25 + i * 5 + s
            picks[2] -= 1
        else:
            break
    
    return answer