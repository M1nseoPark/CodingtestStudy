t = int(input())
for _ in range(t):
    n = int(input())

    i = 2
    answer = {}
    
    while n != 1:
        if n % i == 0:
            n = n // i
            if i not in answer:
                answer[i] = 1
            else:
                answer[i] += 1
        else:
            i += 1

    for k, v in answer.items():
        print(k, v)
            
