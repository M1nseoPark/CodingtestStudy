def solution(name):
    moveUD = 0   # 조이스틱 조작 횟수(상하)
    moveLR = len(name) - 1   # 조이스틱 조작 횟수(좌우)
    n = len(name)
    
    for i in range(n):
        moveUD += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
        
        next = i + 1
        while next < n and name[next] == 'A':
            next += 1
        
        if next != (i + 1):
            moveLR = min(moveLR, 2*i+n-next, i+2*(n-next))
    
    return moveUD + moveLR