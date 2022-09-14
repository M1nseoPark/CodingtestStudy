n = int(input())
series = []
stack = []
answer = []

for _ in range(n):
    series.append(int(input()))

i = 1
while True:
    if i <= n:
        if (len(stack) != 0) and (stack[-1] == series[0]):
            answer.append('-')
            series.pop(0)
            stack.pop()
        
        stack.append(i)
        answer.append('+')
        i += 1
    else:
        if series[-1] != stack[0]:
            break
        else:
            answer.append('-')
            series.pop(0)
            stack.pop()

if (len(series) == 0) and (len(stack) == 0):
    for i in answer:
        print(i)
else:
    print('NO')
            
            
