def solution(n, s):
    if n > s == 0:
        answer = [-1]
        
    else:
        div = s // n
        mod = s % n
        answer = [div] * n

        for i in range(mod):
            answer[i] += 1

        answer.sort()

    return answer
