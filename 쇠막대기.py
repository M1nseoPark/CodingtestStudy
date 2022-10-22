stick = input()

stack = []
answer = 0

for i in range(len(stick)):
    if stick[i] == '(':
        stack.append(i)
    else:
        if stick[i-1] == '(':   # 레이저일 경우
            stack.pop()
            answer += len(stack)
        else:  
            stack.pop()
            answer += 1

print(answer)
