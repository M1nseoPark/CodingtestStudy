name = input()
kind = {}
for i in name:
    if i in kind:
        kind[i] += 1
    else:
        kind[i] = 1

kind = sorted(kind.items())
answer, rest = '', ''
flag = True

for i in range(len(kind)):
    if kind[i][1] % 2 == 1:
        answer += (kind[i][0] * (kind[i][1] // 2))
        if rest == '':
            rest = kind[i][0]
        else:
            flag = False
            break

    else:
        answer += (kind[i][0] * (kind[i][1] // 2))

if not flag:
    print("I'm Sorry Hansoo")
else:
    print(answer + rest + answer[::-1])
    
    



    
