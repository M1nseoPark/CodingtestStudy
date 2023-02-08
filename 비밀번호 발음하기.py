while True:
    p = input()
    
    if p == 'end':
        break

    v = False
    c = [0, 0]

    answer = True
    for i in range(len(p)):
        flag = 0
        # 모음 하나를 반드시 포함 
        if p[i] in ['a', 'e', 'i', 'o', 'u']:
            v = True
            flag = 1
        else:
            flag = 2

        # 모음이 3개 혹은 자음이 3개 연속으로 오면 안됨 
        if c[0] == flag:
            c[1] += 1
        else:
            c[0] = flag
            c[1] = 1

        if c[1] >= 3:
            answer = False
            break

        # 같은 글자가 연속으로 두 번 오면 안됨
        if i != 0 and p[i-1] == p[i] and (p[i] != 'e' and p[i] != 'o'):
            answer = False
            break

    if not v:
        answer = False

    if answer:
        print('<' + p + '> is acceptable.')
    else:
        print('<' + p + '> is not acceptable.')
    


    
