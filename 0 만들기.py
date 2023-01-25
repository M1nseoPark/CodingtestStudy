t = int(input())
for _ in range(t):
    n = int(input())

    arr = [str(i) for i in range(1, n+1)]
    oper = ['+', '-', ' ']
    answer = []

    def make(d, tmp):
        if d == (n-1):
            tmp += arr[d]
            rst = tmp.replace(' ', '')
            if eval(rst) == 0:
                answer.append(tmp)

        else:
            for i in range(3):
                tmp += (arr[d] + oper[i])
                make(d+1, tmp)
                tmp = tmp[:-2]

    make(0, '')
    answer.sort()
    for i in answer:
        print(i)

    print()
                

        
        
        
