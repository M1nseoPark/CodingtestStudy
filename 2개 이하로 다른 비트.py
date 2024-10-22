def solution(numbers):
    answer = []

    for n in numbers:
        if n % 2 == 0:
            answer.append(n + 1)

        # 홀수를 이진법으로 변환했을때 가장 오른쪽에 있는 '0'을 찾는 것이 중요
        # 가장 오른쪽에 위치한 0의 인덱스가 n이라고 가정하면, n인덱스에 위치한 0을 1로 바꿔주고 n+1에 위치한 1을 0으로 바꿔줌
        else:
            b = '0' + bin(n)[2:]
            b = b[:b.rindex('0')] + '10' + b[b.rindex['0'+2:]]
            answer.append(int(b, 2))

    return answer
