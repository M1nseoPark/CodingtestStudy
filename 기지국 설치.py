import math

def solution(n, stations, w):
    answer = 0
    m = w * 2 + 1
    
    start = 1
    for i in range(len(stations)):
        temp = stations[i] - w - start
        if temp > 0:
            answer += math.ceil(temp / m)
        start = stations[i] + w + 1
    
    if start <= n:
        temp = n - start + 1
        answer += math.ceil(temp / m)

    return answer
