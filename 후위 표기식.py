s = input()

stack = []
answer = ''

for i in s:
    # 피연산자가 들어오면 바로 출력함 
    if i.isalpha():
        answer += i

    # 여는 괄호를 만나면 무조건 스택에 담음 
    elif i == '(':
        stack.append(i)

    # 연산자가 들어오면 자신보다 우선순위가 높거나 같은 것들을 빼고 자신을 스택에 담음
    # 스택은 선입선출이므로 자신보다 우선순위가 높은 것들은 먼저 출력되야 함!
    elif i == '*' or i == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            answer += stack.pop()
        stack.append(i)

    elif i == '+' or i == '-':
        while stack and stack[-1] != '(':
            answer += stack.pop()
        stack.append(i)

    # 닫는 괄호를 만나면 여는 괄호를 만날 때까지 스택에서 출력함 
    elif i == ')':
        while stack and stack[-1] != '(':
            answer += stack.pop()
        stack.pop()

while stack:
    answer += stack.pop()

print(answer)
        
