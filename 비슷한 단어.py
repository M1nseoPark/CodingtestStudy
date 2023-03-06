import copy

n = int(input())
word1 = input()
kind1 = {}
for i in word1:
    if i in kind1:
        kind1[i] += 1
    else:
        kind1[i] = 1

answer = 0
for _ in range(n-1):
    word2 = input()
    kind2 = copy.deepcopy(kind1)
    flag, ex = 0, True

    for i in word2:
        if i in kind2:
            if kind2[i] == 1:
                del kind2[i]
            else:
                kind2[i] -= 1

        else:
            if ex:
                ex = False
            else:
                flag += 1

    if len(kind2) != 0:
        flag += (len(kind2) - 1)
    
    print(flag)
    
    if flag < 1:
        answer += 1

print(answer)

    
