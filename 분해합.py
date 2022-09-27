n = int(input())

flag = False
answer = 0
for i in range(n+1):
    init = i
    result = i

    # 아래 코드는 너무 비효율적임
    # 각 자리 수 더하는 코드 -> sum(map(int, str(i)))
    if i >= 1000000:
        init += i // 1000000
        i = i % 1000000
        
    if i >= 100000:
        init += i // 100000
        i = i % 100000

    if i >= 10000:
        init += i // 10000
        i = i % 10000

    if i >= 1000:
        init += i // 1000
        i = i % 1000

    if i >= 100:
        init += i // 100
        i = i % 100

    if i >= 10:
        init += i // 10
        i = i % 10

    init += i

    if init == n:
        flag = True
        answer = result
        break

if flag:
    print(answer)
else:
    print(0)
    
        
        
