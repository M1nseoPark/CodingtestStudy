from collections import deque

def solution(expression):
    answer = 0
    prior = [['*', '+', '-'], ['*', '-', '+'], ['+', '*', '-'], ['+', '-', '*'],
            ['-', '+', '*'], ['-', '*', '+']]

    for i in range(len(prior)):
        answer = max(answer, abs(calculate(prior[i], expression)))

    return answer

def calculate(prior, expression):
    # 수식 리스트로 만들기 
    exp = deque()
    num = ''
    for k in expression:
        if k.isdigit():
            num += k
        else:
            exp.append(num)
            num = ''
            exp.append(k)
            
    exp.append(num)

    # 계산하기
    for p in prior:
        stack = []
        while len(exp) != 0:
            op = exp.popleft()
            if op == p:
                result = str(eval(stack.pop() + op + exp.popleft()))
                stack.append(result)
            else:
                stack.append(op)
        exp = deque(stack)

    return int(stack[-1])


solution("100-200*300-500+20")

    
