import math

def solution(n, stations, w):
    answer = 0
    signal = []
    v = w * 2 + 1
    
    for i in range(len(stations)):
        s, e = 1, n
        if stations[i] - w > 0:
            s = stations[i] - w
        
        if stations[i] + w <= n:
            e = stations[i] + w
        
        signal.append([s, e])
    
    idx = 1
    
    for i in range(len(signal)):
        if idx > n:
            break
        temp = signal[i][0] - idx
        answer += math.ceil(temp / v)
        idx = signal[i][1] + 1
    
    if idx <= n:
        answer += math.ceil((n - signal[-1][1]) / v)
        
    return answer
