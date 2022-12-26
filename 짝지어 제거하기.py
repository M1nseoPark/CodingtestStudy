def solution(s):
    answer = 0
    stack = []
    for i in range(len(s)):
        if len(stack) == 0 or stack[-1] != s[i]:
            stack.append(s[i])
        elif stack[-1] == s[i]:
            stack.pop()
        
    if len(stack) != 0:
        answer = 0
    else:
        answer = 1

    return answer
