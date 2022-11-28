# -13=-2*(7)+1인데 -13=-2*6+1로 계산함

n = int(input())

if n == 0:
    print(0)

else:
    answer = ''
    while n != 0:
        if n % -2 != 0:
            answer = '1' + answer
            n = n // -2 + 1
        else:
            answer = '0' + answer
            n = n // -2

    print(answer)

