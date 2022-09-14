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
            else:
                if len(stack) == 0:
                    answer = False
                elif stack[-1] == '(' and s[i] == ')':
                    stack.pop()
                elif stack[-1] == '[' and s[i] == ']':
                    stack.pop()

        if len(stack) != 0:
            answer = False
        else:
            answer = True


        if answer:
            print('yes')
        else:
            print('no')

    if end:
        break
    
                
