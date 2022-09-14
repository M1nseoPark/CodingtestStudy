# 예전엔 풀었는데 지금 못풀었어ㅠㅠ

n = int(input())
series = []
stack = []
answer = []
make = True

for _ in range(n):
    series.append(int(input()))

i = 1
while len(series) != 0:
    if len(stack) == 0:
        answer.append('+')
        stack.append(i)
        i += 1
    elif stack[-1] == series[0]:
        answer.append('-')
        stack.pop()
        series.pop(0)
    elif i > n:  ##
        make = False
        break
    else:
        answer.append('+')
        stack.append(i)
        i += 1

if make:
    for i in answer:
        print(i)
else:
    print('NO')
            
            
