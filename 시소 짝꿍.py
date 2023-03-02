def solution(weights):
    pos = [(2, 3), (2, 4), (3, 4), (4, 3), (4, 2), (3, 2)]
    answer = 0

    kind = {}
    for w in weights:
        if w in kind:
            kind[w] += 1
        else:
            kind[w] = 1

    for k, v in kind.items():
        # 본인과 같은 무게의 친구가 있을 경우 
        if v > 1:
            answer += (v * (v - 1)) // 2

        # 본인의 몸무게로 평형을 맞출 수 있는 경우
        for i, j in pos:
            temp = k * i / j   # 180 * 4 = 360 * 2 -> (180 * 4) / 2 = 360
            if temp in kind:
                answer += v * kind[temp]

        kind[k] = 0

    return answer
                
            
            
