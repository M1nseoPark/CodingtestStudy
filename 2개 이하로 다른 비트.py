def solution(numbers):
    answer = []

    for n in numbers:
        if n % 2 == 0:
            answer.append(n + 1)
        else:
            b = '0' + bin(n)[2:]
            b = b[:b.rindex('0')] + '10' + b[b.rindex['0'+2:]]
            answer.append(int(b, 2))

    return answer
