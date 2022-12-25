def count(n):
    sub = []
    for i in range(1, n+1):
        if n % i == 0:
            sub.append(i)
    
    return sub


def solution(brown, yellow):
    sub = count(yellow)
    answer = []
    print(sub)
    
    for i in range(len(sub)):
        yy, yx = sub[i], yellow//sub[i]
    
        rst = ((yy + 2) * 2) + (yx * 2)
        if rst == brown:
            answer = [yx + 2, yy + 2]
            break
                
    return answer
