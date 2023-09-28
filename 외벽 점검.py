from itertools import permutations

def solution(n, weak, dist):
    m = len(weak)
    answer = m + 1
    weak_line = weak + [w+n for w in weak]   # [1,5,6,10] -> [1,5,6,10,13,17,18,22]
    
    for i, start in enumerate(weak):  # 시작점 
        for friends in permutations(dist):
            cnt = 1
            cur = start

            for friend in friends:
                cur += friend
                # 끝까지 도달하지 못했을 때 
                if cur < weak_line[i+m-1]:
                    cnt += 1  # 친구 더 투입 
                    for w in weak_line[i+1:i+m]:
                        if w > cur:
                            cur = w
                            break
                else:
                    answer = min(answer, cnt)
                    break
    
    if answer == (m + 1):
        return -1
    else:
        return answer



