def solution(sequence, k):
    n = len(sequence)
    answer = [0, n]
    left, right = 0, 0
    cur = sequence[0]

    while left <= right and right < n:
        if cur <= k:
            if cur == k and (right - left) < (answer[1] - answer[0]):
                answer = [left, right]
            right += 1
    
            if right < n:
                cur += sequence[right]
        else:
            cur -= sequence[left]
            left += 1
    
    return answer

