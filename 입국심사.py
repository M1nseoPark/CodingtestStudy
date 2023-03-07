def solution(n, times):
    answer = 0
    left = min(times)
    right = max(times) * n

    while left <= right:
        mid = (left + right) // 2
        checked = 0

        for t in times:
            checked += mid // t   # mid 시간 동안 심사 가능한 사람 수 
            if checked >= n:
                break

        if checked >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer
