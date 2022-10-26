# 여는 괄호일 때 값을 곱해주는 건 생각했지만,
# 부호를 어떻게 결정해서 계산해줄 것인지 생각 못함

s = input()

stack = []
temp = 1
result = 0

for i in range(len(s)):
    # 여는 괄호일 때
    if s[i] == '(':
        temp *= 2
        stack.append(s[i])
    elif s[i] == '[':
        temp *= 3
        stack.append(s[i])

    # 닫는 괄호일 때
    elif s[i] == ')':
        if not stack or stack[-1] == '[':
            result = 0
            break

        if s[i-1] == '(':
            result += temp  ##

        temp //= 2   ##
        stack.pop()

    else:
        if not stack or stack[-1] == '(':
            result = 0
            break

        if s[i-1] == '[':
            result += temp  

        temp //= 3
        stack.pop()

    # print(temp, result)

if stack:
    result = 0

print(result)
            
        
