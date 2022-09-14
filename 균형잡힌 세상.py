while True:
    sentence = input().split('. ')
    end = False

    for s in sentence:
        if s[0] == '.':
            end = True
            break
        
        stack = []
        answer = True
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[':
                stack.append(s[i])
            # 괄호 말고 다른 문자열도 있기 때문에 괄호 조건을 넣어줘야 함
            elif s[i] == ')':
                if len(stack) == 0:
                    answer = False
                    break
                elif stack[-1] == '(':
                    stack.pop()
                else:
                    answer = False
                    break
            elif s[i] == ']':
                if len(stack) == 0:
                    answer = False
                    break
                elif stack[-1] == '[':
                    stack.pop()
                else:
                    answer = False
                    break

        if len(stack) != 0:
            answer = False


        if answer:
            print('yes')
        else:
            print('no')

    if end:
        break
    
                
