# 자신의 왼쪽이나 오른쪽 방향에 자기보다 큰 수가 존재하면 마지막까지 남길 수 있음
def solution(a):
    result = [False for _ in range(len(a))]
    lmin, rmin = float('inf'), float('inf')

    for i in range(len(a)):
        if a[i] < lmin:
            lmin = a[i]
            result[i] = True
        if a[-1-i] < rmin:
            rmin = a[-1-i]
            result[-1-i] = True
    
    answer = 0
    for i in range(len(result)):
        if result[i]:
            answer += 1
    
    return answer

