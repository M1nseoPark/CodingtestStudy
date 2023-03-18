from collections import Counter

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
