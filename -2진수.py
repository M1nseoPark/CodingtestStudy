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


    '''
    import math

n = int(input())
answer = ''

while True:
    if n == 0:
        answer += '0'
        break
    
    if n == 1:
        answer += '1'
        break

    if n == -1:
        answer += '11'
        break

    t = math.ceil(n / -2)
    answer += str(n - (-2 * t))
    n = t

print(answer[::-1])
'''
