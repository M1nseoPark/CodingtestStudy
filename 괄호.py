t = int(input())

def vps(s):
    stack = []
    answer = True
    
    for i in str:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                answer = False
                break
            elif stack[-1] == '(':
                stack.pop()

    if len(stack) != 0:
        answer = False

    if answer:
        print('YES')
    else:
        print('NO')
    

for _ in range(t):
    str = input()
    vps(str)


'''
for i in str:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')
'''
