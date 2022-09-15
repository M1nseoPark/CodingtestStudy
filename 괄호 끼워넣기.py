s = input()
answer = 0
stack = []

for i in range(len(s)):
    if s[i] == '(':
        stack.append('(')
    elif s[i] == ')':
        if len(stack) == 0:
            stack.append(')')
        elif stack[-1] == '(':
            stack.pop()
        else:
            stack.append(')')

print(len(stack))
