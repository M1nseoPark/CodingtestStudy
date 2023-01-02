def solution(s):
    answer = 0
    
    for i in range(len(s)):
        temp = s[i:] + s[:i]
        
        stack = []
        flag = True
        for j in range(len(temp)):
            if temp[j] == '(' or temp[j] == '[' or temp[j] == '{':
                stack.append(temp[j])
            else:
                if len(stack) == 0:
                    flag = False
                    break
                
                if stack[-1] == '[' and temp[j] == ']':
                    stack.pop()
                elif stack[-1] == '(' and temp[j] == ')':
                    stack.pop()
                elif stack[-1] == '{' and temp[j] == '}':
                    stack.pop()
                else:
                    flag = False
                    break
        
        if len(stack) != 0:
            flag = False
        
        if flag:
            answer += 1
    
    return answer
