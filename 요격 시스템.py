def solution(targets):
    stack = []
    targets.sort(key=lambda x:(x[1], x[0]))   # 끝나는 시간 순으로 정렬하는 이유는?
    
    for i in range(len(targets)):
        s, e = targets[i]
        if stack and stack[-1][1] > targets[i][0]:
            stack[-1][0] = targets[i][0]
        else:
            stack.append(targets[i])
            
    return len(stack)