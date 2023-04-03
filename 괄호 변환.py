def solution(p):
    answer = ''
    if decide(p):
        return p

    answer = dfs(p)
    return answer


def divide(p):
    left, right = 0, 0
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1

        if left == right:
            u = p[:i+1]
            if i + 1 < len(p):
                v = p[i+1:]
            else:
                v = ''
                
    return u, v


def decide(p):
    stack = []
    for i in range(len(p)):
        if p[i] == '(':
            stack.append(p[i])
        else:
            if len(stack) == 0:
                return False
            stack.pop()

    if len(stack) != 0:
        return False
    return True


def dfs(p):
    result = ''
    if len(p) == 0:
        return ''

    u, v = divide(p)
    if decide(u):
        result = u + dfs(v)
    else:
        temp = '('
        temp += dfs(v)
        temp += ')'

        u = u[1:-1]
        for i in range(len(u)):
            if u[i] == '(':
                temp += ')'
            else:
                temp += '('

        result += temp

    return result


    


    
            
