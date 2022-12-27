import math

def solution(n,a,b):
    r, d = 1, 2
    while True:
        ar = math.ceil(a / (d**r))
        br = math.ceil(b / (d**r))
        
        if ar == br:
            break
        
        r += 1
        
    return r
