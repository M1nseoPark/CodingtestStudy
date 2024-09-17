from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for k in course:
        candidates = []

        for order in orders:
            for li in combinations(order, k):
                res = ''.join(sorted(li))
                candidates.append(res)
        
        sorted_candidates = Counter(candidates).most_common()
        # [('AC', 4), ('CD', 3), ('CE', 3), ('DE', 3), ('BC', 2), ('BF', 2), ('BG', 2), ('CF', 2), ('CG', 2), ('FG', 2), ('AD', 2), ('AE', 2), ('AB', 1), ('AF', 1), ('AG', 1), ('AH', 1), ('CH', 1), ('DH', 1), ('EH', 1)]

        result = []
        for order, cnt in sorted_candidates:
            # 최소 2명 이상의 손님으로부터 주문 & 가장 많이 함께 주문
            if cnt > 1 and cnt == sorted_candidates[0][1]:
                result.append(order)
        
        answer += result
    
    return answer


