n = int(input())

if n != 1:
    answer = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            n //= i
            answer.append(i)
        
        else:
            i += 1

    answer.append(n)

    for i in answer:
        print(i)
