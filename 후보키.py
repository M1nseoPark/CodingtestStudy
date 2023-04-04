from itertools import combinations

def solution(relation):
    n = len(relation)
    m = len(relation[0])

    combi = []
    for i in range(1, n+1):
        combi.extend(combinations(range(m), i))

    key = []
    for c in combi:
        temp = [tuple([item[i] for i in c]) for item in relation]

        if len(temp) == n:
            flag = True

            for k in key:
                if set(k).issubset(set(c)):
                    flag = False
                    break

            if flag:
                key.append(c)

    return len(key)
