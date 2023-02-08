import sys

s = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()

answer = ''
stack = []
for i in s:
    stack.append(i)
    
    if len(stack) >= len(b) and ''.join(map(str, stack[-len(b):])) == b:
        for j in range(len(b)):
            stack.pop()

answer += ''.join(map(str, stack))
if len(answer) == 0:
    print('FRULA')
else:
    print(answer)


