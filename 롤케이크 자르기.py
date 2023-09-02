# [1,2,1,3,1,4,1,2] 같은 리스트를 절반으로 나눴을 때, 두 조각의 숫자 종류의 개수가 같도록 나누는 방법 
from collections import Counter

# 모범답안 
def solution(topping):
    dic = Counter(topping)
    s = set()
    answer = 0

    for i in topping:
        dic[i] -= 1
        s.add(i)

        if dic[i] == 0:
            del dic[i]

        if len(dic) == len(s):
            answer += 1

    return answer


# 내가 푼 다른 풀이 
def solution(topping):
    llst, rlst = [], []
    lset, rset = set(), set()
    n = len(topping)
    answer = 0
    
    for i in range(n):
        lset.add(topping[i])
        rset.add(topping[n-1-i])
        
        llst.append(len(lset))
        rlst.append(len(rset))
    
    for i in range(n-1):
        if llst[i] == rlst[n-2-i]:
            answer += 1

    return answer
